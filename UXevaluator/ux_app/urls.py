from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("signup/", register_view, name="signup"),
    path("home/", home, name="home"),
    path("login/", login_view, name="login"),
    path('logout/', logout_view, name='logout'),
    path('', include('django.contrib.auth.urls')),
]
