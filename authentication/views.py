from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer, UserSerializer
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from rest_framework_simplejwt import views as jwt_views


# Create your views here.
class UserListView(generics.ListAPIView):
    # queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    def get_queryset(self):
        user = self.request.user
        return get_user_model().objects.filter(id=user.id)


class CustomUserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        # print(request.data['password'])
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = {}
                json["username"] = serializer.data["username"]
                json["password"] = request.data["password"]
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
