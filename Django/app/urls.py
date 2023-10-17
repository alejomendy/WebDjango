from django.urls import path
from .views import main_page, login, register, post, newpost, deletepost, deletecomment

app_name = 'nombreApp'
urlpatterns = [
    path('', main_page, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name= 'register'),
    path('post/<int:id>', post, name='post'),
    path('newpost/', newpost, name='newpost'),
    path('post/deletepost/<int:id>', deletepost, name='deletepost'),
    path('post/deletecomment/<int:id>', deletecomment, name='deletepost'),
]