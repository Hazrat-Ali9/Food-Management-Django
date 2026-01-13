from django.contrib import admin
from django.urls import path
from . import views
# urls py
app_name = 'contact'

urlpatterns = [
    path('email/', views.emailView, name='email'),
    path('success/', views.successView, name='success'),
]
