from django.urls import path
from authen import views

urlpatterns = [
    path('', views.Home, name="Home"),
 
]