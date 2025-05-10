from django.urls import path
from .views import home_view, post_list, create_post, edit_post, delete_post

urlpatterns = [
    path('', home_view, name='home'),
    path('posts/', post_list, name='post_list'),
    path('posts/new/', create_post, name='create_post'),
    path('posts/<int:post_id>/edit/', edit_post, name='edit_post'),
    path('posts/<int:post_id>/delete/', delete_post, name='delete_post'),
]
