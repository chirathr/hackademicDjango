from rest_framework.serializers import ModelSerializer
from .models import Article


class ArticleCreateSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
        ]


class ArticleListSerializer(ModelSerializer):

    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'content',
            'created_by',
            'image',
        ]


class ArticleDetailSerializer(ModelSerializer):

    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'content',
            'created_by',
            'image',
        ]