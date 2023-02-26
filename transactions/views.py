from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework import permissions
import plaid
from transactions.lib.plaid import PlaidIntegration
from rest_framework.response import Response
import json

class CreateLinkToken(APIView):
    """
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
      try:
        plaid_client = PlaidIntegration()
        lt = plaid_client.create_link_token(user=None)
        return Response(lt)

      except plaid.ApiException as e:
          return Response(json.loads(e.body), status=status.HTTP_400_BAD_REQUEST)

