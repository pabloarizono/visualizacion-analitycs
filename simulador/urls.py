"""
URL configuration for simulador project.

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
from django.contrib import admin
from django.urls import path 
from aplicacion1.views import prueba
from aplicacion2.views import dashboard
from aplicacion3.views import dashboard_data_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/', prueba, name='hola'),
    path('dash_app/', dashboard, name='dashboard'),
    path('api/dashboard_data/', dashboard_data_api, name='dashboard_data_api'),
   
    
]
