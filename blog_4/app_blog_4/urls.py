from django.urls import path
from .import views

app_name='app_blog_4' 

urlpatterns = [    
    path('', views.index, name='index'),
    path('generales/', views.generales, name='generales'),
    path('programacion/', views.programacion, name='programacion'),
    path('videojuegos/', views.videojuegos, name='videojuegos'),
    path('tecnologia/', views.tecnologia, name='tecnologia'),
    path('tutoriales/', views.tutoriales, name='tutoriales'),
    path('<slug:slug>/', views.detalle_post, name='detalle_post'),
    
]
