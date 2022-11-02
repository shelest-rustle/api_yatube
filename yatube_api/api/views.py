from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from posts.models import Comment, Group, Post, User
from .serializers import (CommentSerializer, GroupSerializer, PostSerializer,
                          UserSerializer)
from .permissions import IsAuthorOrReadOnly


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=get_object_or_404(Post, pk=self.kwargs['post_id'])
        )

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        queryset = Comment.objects.filter(post=post.id)
        return queryset


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
