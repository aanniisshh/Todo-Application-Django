from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import models

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



# Create your views here.

class CreateTodo(APIView):
    @csrf_exempt
    def post(self, request):
        print(request.data.get('mane'))
        models.TodoList.objects.create(
            title=request.data.get('title'),
            content=request.data.get('content'),
            due_date=request.data.get('due_date')
        )
        return Response(data={"message": "Todo created successfully"}, status=status.HTTP_201_CREATED)

class GetTodo(APIView):
    @csrf_exempt
    def get(self, request):
        dic = {}
        dic['response'] = []

        tood = models.TodoList.objects.all()
        for i in tood:
            json_obj = dict(
                title = i.title,
                content = i.content,
                created = i.created,
                due_date = i.due_date

            )
            dic['response'].append(json_obj)

        return Response(data=dic, status=status.HTTP_201_CREATED)




@csrf_exempt
def list_view(request, *args, **kwargs):
    data =  {
        "id" : 1,
        "name" : "Maneesh"
    }
    return JsonResponse(data)

