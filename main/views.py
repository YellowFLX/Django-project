from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import Task
from .forms import TaskForm


def index(request):
    return render(request, 'main/index.html', {'title': 'Главная'})

def app(request):
    tasks = Task.objects.order_by('id')
    return render(request, 'main/app.html', {'title': 'Главная', 'tasks': tasks})

def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app')
        else:
            error = 'Некорректная задача'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)

@csrf_exempt
def complete(request, pk):
    test = Task.objects.get(id=pk)
    test.done = True
    test.save()
    return HttpResponseRedirect('/app')


