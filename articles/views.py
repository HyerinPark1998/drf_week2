from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from articles.models import Articles
from articles.serializers import ArticlesSerializers
from drf_yasg.utils import swagger_auto_schema

# Create your views here.


class ArticlesList(APIView):
    def get(self, request, format=None):
        articles = Articles.objects.all()
        serializers = ArticlesSerializers(articles, many=True)
        return Response(serializers.data)

    @swagger_auto_schema(request_body=ArticlesSerializers)
    def post(self, request, format=None):
        serializers = ArticlesSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            print(serializers.errors)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):

    def get(self, request, article_id, format=None):
        article = get_object_or_404(Articles, id=article_id)
        serializers = ArticlesSerializers(article)
        return Response(serializers.data)

    def put(self, request, article_id, format=None):
        article = get_object_or_404(Articles, id=article_id)
        serializers = ArticlesSerializers(article, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, article_id, format=None):
        article = get_object_or_404(Articles, id=article_id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
