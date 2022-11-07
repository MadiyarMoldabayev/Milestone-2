"""CRUDOperation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showemp, name = "showemp"),
    path('Insert',views.insertemp,name="insertemp"),
    path('InsertPatient', views.insertpatient, name="insertpatient"),
    path('editpatient/<int:id>', views.editpatient, name="editpatient"),
    path('UpdatePatient/<int:id>',views.updatepatient, name="updatepatient"),
    path('edit/<int:id>', views.editemp,name="editemp"),
    path('Update/<int:id>',views.updateemp, name="updateemp"),
    path('DeletePatient/<int:id>', views.delpatient, name="delpatient"),
    path('Delete/<int:id>', views.delemp, name="delemp"),
]
