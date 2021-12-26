"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView
from .views import ArticleListView,ArticleDetailView,createArticle,updateArticle,ArticleDeleteView
app_name='articles'
urlpatterns = [
    path('', ArticleListView.as_view(),name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('post/create', createArticle, name='create'),
    path('post/edit/<int:pk>', updateArticle, name='edit'),
    path('post/delete/<int:pk>',ArticleDeleteView.as_view(), name='delete'),
    path('post/<slug:slug>', ArticleDetailView.as_view(),name='post'),
]
