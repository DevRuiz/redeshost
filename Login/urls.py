from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
# from rest_framework import routers, serilizers, viewsets
from Login.views import CustonAuthToken

from Login import views

urlpatterns = [
    re_path(r'Login/$', CustonAuthToken.as_view()),
    re_path(r'login_lista/$', views.LoginList.as_view()),
    #Hola soy Fer
]