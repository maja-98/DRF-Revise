from rest_framework import serializers
from blog.models import Post


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['published', 'slug', 'category']


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['published', 'slug', 'category', 'author']
