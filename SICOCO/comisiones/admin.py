from django.contrib import admin
from comisiones.models import Empleado,Pedido,Comision

class ComisionAdmin(admin.ModelAdmin):
    readonly_fields = ('monto',)
    fields = ('empleado', 'periodo_inicio', 'periodo_fin', 'monto')  # Asegurarse de que 'monto' se muestre

    def get_readonly_fields(self, request, obj=None):
        # Se asegura de que 'monto' sea de solo lectura al crear o editar
        readonly = list(self.readonly_fields)
        return readonly
    

admin.site.register(Empleado)
admin.site.register(Pedido)
admin.site.register(Comision,ComisionAdmin)
