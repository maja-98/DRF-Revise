from rest_framework import generics
from blog.models import Post
from .serializers import PostCreateSerializer, PostListSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import PostUserWritePermission


class PostList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.postobjects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostCreateSerializer
        else:
            return PostListSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostListSerializer
        else:
            return PostCreateSerializer
