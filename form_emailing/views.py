from django.shortcuts import HttpResponse
from rest_framework.views import APIView


class SendEmail(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data['email']
        return HttpResponse('Cool')
