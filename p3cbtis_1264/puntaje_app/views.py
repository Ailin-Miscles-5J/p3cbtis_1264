from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request,"index.html")

def contactos (request):
    return render(request,"contactos.html")

def empleado (request):
    return render(request,"empleado.html")

def distribuidores (request):
    return render(request,"distribuidores.html")

def productos (request):
    return render(request,"productos.html")

def sucursal (request):
    return render(request,"sucursal.html")
