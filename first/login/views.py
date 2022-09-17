from rest_framework import viewsets
from rest_framework import fields,serializers
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from . import serializers
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.UserSerializer
    queryset = get_user_model().objects.all()