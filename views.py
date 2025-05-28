from django.shortcuts import render, get_object_or_404, redirect
from .models import Paciente 
from .forms import PacienteForm

def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/lista.html', {'pacientes': pacientes})

def crear_paciente(request):
    form = PacienteForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('pacientes:lista')
    return render(request, 'pacientes/formulario.html', {'form': form})

def editar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    form = PacienteForm(request.POST or None, instance=paciente)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('pacientes:lista')
    return render(request, 'pacientes/formulario.html', {'form': form})

def eliminar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    paciente.delete()
    return redirect('pacientes:lista')

