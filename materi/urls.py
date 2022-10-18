from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),  
    path('applet/', views.applet, name='applet'),
    path('bab1/', views.bab1, name='bab1'),
    path('bab2/', views.bab2, name='bab2'),
    path('bab3/', views.bab3, name='bab3'),
    path('bab4/', views.bab4, name='bab4'),
    path('profile/', views.profile, name='profile'),
    path('mahasiswa/', views.mahasiswa, name='mahasiswa'),
    
]