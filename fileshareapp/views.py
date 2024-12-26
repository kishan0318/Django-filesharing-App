import os
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.parsers import MultiPartParser
from django.contrib.auth.models import User
from .serializers import FileListSerializer
from django.http import FileResponse


# Create your views here.

def home(request):
    return render(request, "home.html")

def download(request, uid):
    zip_path = f"public/static/shareable_zip/{uid}.zip"
    if os.path.exists(zip_path):
        return FileResponse(open(zip_path, 'rb'), as_attachment=True, filename=f"{uid}.zip")
    return render(request, 'download.html', context={'uid': uid, 'error': 'File not found'})



class HandleFileView(APIView):
    parser_classes = [MultiPartParser]
    def post (self , request):
        data = request.data
        print(data)
        serializer = FileListSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 200,
                'message' : 'File uploaded Successfully',
                'data' : serializer.data
            })
        return Response({
                'status': 200,
                'message' : 'Something went wrong',
                'data' : serializer.errors
            })
