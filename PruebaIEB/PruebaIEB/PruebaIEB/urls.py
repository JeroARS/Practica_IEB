"""
URL configuration for PruebaIEB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.shortcuts import redirect
from App import views

urlpatterns = [
    path('', lambda request: redirect('crear_producto', permanent=False)),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('detalle_producto/', views.detalle_producto, name='detalle_producto'),
    path('mostrar_informacion/', views.mostrar_informacion, name='mostrar_informacion'),

]


