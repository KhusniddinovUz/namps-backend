from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from django.core.mail import send_mail


class SendEmail(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data['email']
        message = request.data['message']
        send_mail('Message for Nam PM', f'From {email} : {message}', None, ['khusniddinovuz@gmail.com'])
        return HttpResponse('Cool')
