from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import UserViewSet, PostViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='viewset')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls