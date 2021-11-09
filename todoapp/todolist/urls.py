from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.list_view),
    path('create/', views.CreateTodo.as_view()),
    path('get/', views.GetTodo.as_view())
]