from rest_framework import serializers

from posts.models import Comment, Group, Post, User


class UserSerializer(serializers.ReadOnlyField):
    class Meta:
        model = User
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')
    group = serializers.SlugRelatedField(
        read_only=True, slug_field='slug')

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('author',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('author',)
