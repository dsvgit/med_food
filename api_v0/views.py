from rest_framework import viewsets
from api_v0 import serializers
from django.contrib.auth.models import User, Group
from rest_framework.decorators import detail_route, list_route, api_view
from rest_framework.response import Response
from oauth2_provider.models import AbstractApplication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from calc.models import Food


class FoodViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Food.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.FoodSerializer
        return serializers.FoodSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        return User.objects.all().order_by('-date_joined')


class CurrentUserView(viewsets.ViewSet):
    def list(self, request):
        serializer = serializers.UserSerializer(request.user, many=False, context={'request': request})
        return Response(serializer.data)


# class CurrentUserViewSet(viewsets.GenericViewSet):
#     queryset = User.objects.all().first()
#     serializer_class = serializers.UserSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     serializer_class = serializers.UserSerializer
#
#     def get_queryset(self):
#         # username = self.kwargs['id']
#         return User.objects.filter(user__id=username)
# self.request.user.id


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
