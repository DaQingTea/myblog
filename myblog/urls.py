"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from mysite.views import (
    IndexView, CategoryView, TagView, PostDetailView, SearchView, AuthorView)
from comment.views import CommentView
from config.views import links

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('category/<int:category_id>/', CategoryView.as_view(), name='category_list'),
    path('tag/<int:tag_id>/', TagView.as_view(), name='tag_list'),
    path('post/<int:post_id>.html/', PostDetailView.as_view(), name='post_detail'),
    path('links/',links, name='links'),
    path('search/', SearchView.as_view(), name='search'),
    path('author/<int:owner_id>', AuthorView.as_view(), name='author'),
    path('comment/', CommentView.as_view(), name='comment'),
    path('admin/', admin.site.urls, name='admin'),
    ]
