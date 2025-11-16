from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/<int:pk>/edit/', views.edit_task, name='edit_task'),
    path('task/<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('create/', views.create_task, name='create_task'),
    path('search/', views.search, name='search'),
    path('task/<int:pk>/toggle/', views.toggle_task, name='toggle_task'),
]
