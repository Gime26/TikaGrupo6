from django.shortcuts import render, redirect
from .models import Paciente
from .forms import PacienteForm

def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/lista.html', {'pacientes': pacientes})

def crear_paciente(request):
    pass

def editar_paciente(request, id):
    pass

def eliminar_paciente(request, id):
    pass

