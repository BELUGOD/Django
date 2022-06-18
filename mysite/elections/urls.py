from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('hobby/', views.hobby),
    path('residence/', views.residence),
    path('sch_fri/', views.sch_fri),
    path('travel/', views.travel),
    path('TMI/', views.TMI),
]
