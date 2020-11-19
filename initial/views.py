from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import ToDo


def home(request):
    todo_items = ToDo.objects.all().order_by("-added_date")
    return render(request, 'initial/index.html', {'todo_items': todo_items})


def add_todo(request):
    text = request.POST.get('content')
    todo = ToDo.objects.create(text=text, added_date=timezone.now())
    return HttpResponseRedirect("/")


def delete_todo(request, pk):
    ToDo.objects.get(id=pk).delete()
    return HttpResponseRedirect("/")
