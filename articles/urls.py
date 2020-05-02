from django.urls import path
from .views import ArticlesListAPIView

# TODO: article/ url
urlpatterns = [
    path('articles/', ArticlesListAPIView.as_view(), name='articles-list'),
]
