from django.urls import path    
from .views import playground

urlpatterns = [
    path('hello/', playground),
]