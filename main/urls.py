from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('app', views.app, name='app'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),  
    path('complete/<int:pk>/', views.complete),  
]
