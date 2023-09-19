from django.urls import path
from . import views

urlpatterns = [
    path('', views.startpage),
    path('landing/', views.landing),
]