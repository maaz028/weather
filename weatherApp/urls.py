from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [

    path('', views.weather, name='weather'),
    path('check', views.check_weather, name='check')
]
