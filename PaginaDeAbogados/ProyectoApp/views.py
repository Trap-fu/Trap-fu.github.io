from django.shortcuts import render


# Create your views here.

def home(request):
    
    return render(request, "ProyectoApp/home.html")

def servicios(request):
    
    return render(request, "ProyectoApp/servicios.html")

def abogados(request):
    
    return render(request, "ProyectoApp/abogados.html")

def contacto(request):
    
    return render(request, "ProyectoApp/contacto.html")

