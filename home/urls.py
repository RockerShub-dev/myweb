from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='main'),
    path("about", views.about, name='about'),
    path("help", views.help, name='help'),
    path("members", views.members, name='members')
]
