from jwtauth.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User

class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires jwt authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        """
        Return a list of all users.
        """
        serializer = UserSerializer(User.objects.all(), many=True)
        data = [user for user in serializer.data]
        return Response(data)


