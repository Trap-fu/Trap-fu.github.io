from django.urls import path

from ProyectoApp import views

urlpatterns = [
    path('',views.home, name="Home"),
    path('servicios',views.servicios, name="Servicios"),
    path('abogados',views.abogados, name="Abogados"),
    path('contacto',views.contacto, name="Contacto"),
]