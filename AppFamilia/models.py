from django.db import models

class Familia(models.Model):

    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    dni=models.IntegerField()
    fechaDeNacimiento=models.DateField()
