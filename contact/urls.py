from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('contact-form/', views.contact_form, name='contact_form')
]