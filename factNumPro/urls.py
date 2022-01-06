from django.contrib import admin
from django.urls import path
from factApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.fact, name='fact')
]
