from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles_list, name='articles_list'),
    path('create_article/', views.create_article, name='create_article'),
]
