from xml.etree.ElementInclude import include
from . import views
from apps import members

from django.urls import path
from django.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('add/', views.add, name='add'),
]