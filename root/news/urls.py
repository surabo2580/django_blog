from django.urls import path
from . import  views


urlpatterns = [
    path('postcomment', views.postComment, name='postComment'),
    path('<str:slug>',views.newsPost,name='newsPost'),
    path('',views.newsHome,name='newsHome'),
]