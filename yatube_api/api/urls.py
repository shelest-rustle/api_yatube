from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from api.views import CommentViewSet, GroupViewSet, PostViewSet


router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(
    r'posts/(?P<post_id>[1-9]\d*)/comments',
    CommentViewSet, basename='comments'
)

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token, name='api-token'),
    path('v1/', include(router.urls))
]
