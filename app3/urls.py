from django.contrib import admin
from django.urls import path
from app3 import views

urlpatterns = [
    path('', views.index, name='home'),
    path("service/", views.service, name="service")
]