from django.shortcuts import render
from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer

# Create your views here.
class ArticlesListAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetailAPIView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'pk'
