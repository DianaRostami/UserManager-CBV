from django.urls import path
from .views import UserListCreateAPIView




urlpatterns = [
    # path('users/', UserManagerAPI.as_view(), name="user-list"),
    # path('users/<int:pk>', UserManagerAPI.as_view(), name='user-id')
    path("user/", UserListCreateAPIView.as_view(), name="user-list-create")
]