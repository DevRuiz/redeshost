from django.shortcuts import render

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics

#Importar el modelo
from Login.models import Login
from Login.serializer import LoginSerializers

class LoginList(APIView):
    #METODO GET PARA SOLICTAR INFO
    def get(self, request, format = None):
        print("Metodo get filter")
        queryset = Login.objects.filter(delete = False)
        #many = True si aplica si retorno multiples objetos
        serializer = LoginSerializers(queryset, many = True)
        return Response(serializer.data)

    def post(self,request, format = None):
        serializer = LoginSerializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



class CustonAuthToken(ObtainAuthToken):

    def post(self, request, * args, **kwars):
        serializer = self.serializer_class (data = request.data,
                                            context = {
                                                    'request': request,
                                                    }
                                            )
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })
