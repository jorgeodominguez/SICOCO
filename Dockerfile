FROM python:3

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y apache2
RUN apt-get install -y libapache2-mod-wsgi-py3
RUN apt-get install -y pkg-config
RUN apt-get install -y libpq5
RUN apt-get install -y gcc     

# Limpia la caché de apt
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Configure timezone
ENV TZ=America/Mexico_City
RUN ln -snf  /etc/l/usr/share/zoneinfo/$TZocaltime && echo $TZ > /etc/timezone

WORKDIR /SICOCO

COPY ./requirements.txt /SICOCO/requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install -r /SICOCO/requirements.txt

# Cambia al directorio donde se encuentra manage.py
WORKDIR /SICOCO/SICOCO
EXPOSE 80

CMD [ "apachectl", "-DFOREGROUND","python3","runserver","0.0.0.0:8000" ]