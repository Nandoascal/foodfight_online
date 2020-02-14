from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='foodfight-home'),
    path('about/', views.about, name='foodfight-about')
]
