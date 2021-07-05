from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

from .models import Products
from .my_serializer import productSerializer
import pandas as pd

# Create your views here.

# def index(request):
#     return HttpResponse('<h1>Wellcome to Product Api section...</h1>')

class productList(APIView):
    
    def get(self, request):
        item = Products.objects.all()
        serializer = productSerializer(item, many=True)
        return Response(serializer.data)


    def post(self, request):
        seril = productSerializer(data=request.data)
        if seril.is_valid():
            seril.save()
            return Response(seril.data, status=status.HTTP_201_CREATED)
        return Response(seril.errors, status=status.HTTP_400_BAD_REQUEST)


