from django.urls import path

from .import views
from django.conf.urls import include

urlpatterns = [
    path('',views.index, name="index"),
    path('contact/',views.contact, name="contact"),
    path('entertainment/', views.entertainment, name='entertainment'),
    path('health/', views.health, name='health'),
    path('business/', views.business, name='business'),
    path('sports/', views.sports, name='sports'),
    path('technology/', views.technology, name='technology'),
    path('science/', views.science, name='science'),
]