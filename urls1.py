
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.homepage,name="homepage"),
    path('check',views.getdata,name="getdata")

]
