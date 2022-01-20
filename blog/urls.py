from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.blogHome, name="blogHome"),
    path('<str:slug>/', views.blogPost, name="blogPost"),

    path('postComment', views.postComment, name="postComment"),
]