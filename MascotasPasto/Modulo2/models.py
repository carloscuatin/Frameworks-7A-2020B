from django.db import models

# Create your models here.


class afiliados(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField()
    apellidos = models.TextField()
    numero_movil = models.IntegerField()
    direccion = models.TextField()
    email = models.TextField()
    id_ciudad = models.ForeignKey(
        'ciudades', on_delete=models.SET_NULL, null=True)
    estado = models.CharField(max_length=1)
    fecha_creacion = models.DateField()
    fecha_modificacion = models.DateField()


class paises(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10)
    nombre = models.TextField()
    abreviatura = models.CharField(max_length=4)
    estado = models.CharField(max_length=1)
    fecha_creacion = models.DateField()
    fecha_modificacion = models.DateField()


class ciudades(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10)
    nombre = models.TextField()
    abreviatura = models.CharField(max_length=4)
    id_pais = models.ForeignKey(
        'paises', on_delete=models.SET_NULL, null=True)
    estado = models.CharField(max_length=1)
    fecha_creacion = models.DateField()
    fecha_modificacion = models.DateField()
