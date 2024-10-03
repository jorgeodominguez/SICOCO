from django.db import models

from django.db import models
from datetime import date

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_ingreso=models.DateField("Fecha de Ingreso",default=date.today)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Pedido(models.Model):
    empleado = models.ForeignKey('comisiones.Empleado', on_delete=models.CASCADE, related_name='pedidos')
    pedido=models.CharField('Numero de Pedido',max_length=10,default='')
    fecha = models.DateField("Fecha de comision",default=date.today)
    comision=models.DecimalField('Cantidad de Comision',max_digits=5,decimal_places=2,default=0)

    def __str__(self):
        return f"Pedido #{self.pedido} - {self.empleado} - {self.comision}"

class Comision(models.Model):
    empleado = models.ForeignKey('comisiones.Empleado', on_delete=models.CASCADE, related_name='comisiones')
    monto = models.DecimalField(max_digits=10, decimal_places=2,editable=False)
    periodo_inicio = models.DateField()
    periodo_fin = models.DateField()

    def __str__(self):
        return f"Comisión de {self.empleado} de {self.periodo_inicio} a {self.periodo_fin} = {self.monto}"
    
    def save(self, *args, **kwargs):
        # Solo calcular la comisión si ambas fechas están establecidas
        if self.periodo_inicio and self.periodo_fin:
            self.calcular_comision()
        super().save(*args, **kwargs)

    def calcular_comision(self):
        # Obtener los pedidos del empleado dentro del periodo seleccionado
        pedidos = Pedido.objects.filter(
            empleado=self.empleado,
            fecha__gte=self.periodo_inicio,
            fecha__lte=self.periodo_fin
        )
        # Calcular la suma total de los pedidos
        total_comision = sum(pedido.comision for pedido in pedidos)

        # Actualizar el monto de la comisión
        self.monto = total_comision
