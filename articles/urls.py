from django.urls import path
from .views import ArticlesListAPIView, ArticleDetailAPIView

# TODO: article/ url
urlpatterns = [
    path('<int:pk>/', ArticleDetailAPIView.as_view(), name='article-detail'),
    path('', ArticlesListAPIView.as_view(), name='articles-list'),
]
