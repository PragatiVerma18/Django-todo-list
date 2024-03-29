from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('add', views.addtodo,name = "add"),
    path('complete/<todo_id>',views.completetodo,name='complete'),
    path('deletecomplete', views.deleteCompleted,name='deletecomplete'),
    path('deleteall',views.deleteAll, name ='deleteall'),
    path('endtodo/<todo_id>',views.endtodo,name="endtodo")
]