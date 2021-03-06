from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('base/', views.base, name='base'),
    path('login/', views.user_login, name='user_login' ),
    path('logout/', views.user_logout, name='logout'),
    path('special/',views.special, name='special')
]