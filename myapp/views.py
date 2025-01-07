from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from .models import User
from .serializer import UserSerializer
from rest_framework import permissions

# Create your views here.

# class UserManagerAPI(APIView):

#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def get(self,request, pk=None):
#         if pk:
#             return self.retrieve_user(request, pk)
#         else:
#             return self.list_users(request)
        
#     def retrieve_user(self, request, pk):
#         user = User.objects.get(pk=pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)

#     def list_users(self, request):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         user = User.objects.get(pk=pk)
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         user = user.objects.get(pk=pk)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class UserListCreateAPIView(ListCreateAPIView):
    serializer_class =  UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    