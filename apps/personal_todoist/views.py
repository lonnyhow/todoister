from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'personal_todoist/index.html', {'tasks': tasks})

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('index')
    else:
        form = TaskForm()
    return render(request, 'personal_todoist/create.html', {'form': form})

@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm(instance=task)

    return render(request, 'personal_todoist/edit.html', {'form': form})

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return redirect('index')

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    return render(request, 'personal_todoist/detail.html', {'task': task})

@login_required
def search(request):
    query = request.GET.get('q', '')
    results = Task.objects.filter(user=request.user, title__icontains=query)
    return render(request, 'personal_todoist/search.html',
                  {'results': results, 'query': query})

def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.is_completed = not task.is_completed
        task.save()
    return redirect('index')