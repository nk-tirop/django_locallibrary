from django.urls import path
from . import views
from django.shortcuts import render


urlpatterns = [
     path('', views.index, name='index'),
     path('books/', views.BookListView.as_view(), name='books'),
     path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]