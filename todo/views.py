from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
from .models import todo
from .forms import todoform

def index(request):
  todo_list = todo.objects.order_by('id')
  form = todoform()
  context ={'todo_list' : todo_list, 'form':form}
  
  return render(request, 'todo/index.html', context)

@require_POST
def addtodo(request):
  form = todoform(request.POST)

  if form.is_valid():
    new_todo = todo(text=request.POST['text'])
    new_todo.save()

  return redirect('index')

def completetodo(request, todo_id):
  ctodo = todo.objects.get(pk=todo_id)
  ctodo.complete= True
  ctodo.save()

  return redirect('index')

def deleteCompleted(request):
  todo.objects.filter(complete__exact = True).delete()

  return redirect('index')

def deleteAll(request):
  todo.objects.all().delete()

  return redirect('index')

def endtodo(request,todo_id):
  ctodo = todo.objects.get(pk=todo_id)
  ctodo.delete()
  return redirect('index')