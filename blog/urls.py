from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('creaking/', views.creaking, name='creaking'),
    path('breeze/', views.breeze, name='breeze'),
]