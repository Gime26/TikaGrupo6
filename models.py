from django.db import models

class Pacientes(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    dni = models.CharField(max_length=10, unique=True)
    fecha_nacimiento = models.DateField()
    obra_social = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    genero = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Femenino')])

    def __str__(self):
        return f"{self.nombre} {self.apellido}"