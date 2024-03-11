from django.shortcuts import render
from .models import Employee
from .serializer import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class EmployeeView(APIView):
    def post(self,request):
        serializer=EmployeeSerializer()
        if request.method=='POST':
            serializer=EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        emp=Employee.objects.all()
        serializer=EmployeeSerializer(emp,many=True)
        return Response(serializer.data)
    
    def put(self,request,pk):
        o=Employee.objects.get(eid=pk)
        if request.method=='PUT':
            serializer=EmployeeSerializer(o,data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk):
        o=Employee.objects.get(eid=pk)
        if request.method=='PATCH':
            serializer=EmployeeSerializer(o,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self,request,pk):
        o=Employee.objects.get(eid=pk)
        if request.method=='DELETE':
            o.delete()
            return Response (status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

