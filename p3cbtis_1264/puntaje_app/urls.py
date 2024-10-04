from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("contactos/",views.contactos,name="contactos"),
    path("empleado/",views.empleado,name="empleado"),
    path("productos/",views.productos,name="productos"),
    path("distribuidores/",views.distribuidores,name="distribuidores"),
    path("sucursal/",views.sucursal,name="sucursal"),

]
