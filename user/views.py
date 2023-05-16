from rest_framework import viewsets
from .models import User, ProfilePermission
from .serializers import UserSerializer, ProfileSerializer
from .permissions import UserPermission


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = ProfilePermission.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [UserPermission]
