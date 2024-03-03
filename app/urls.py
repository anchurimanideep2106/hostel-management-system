from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path("",views.first1, name='app'),
    path("login1",views.logina, name='app'),
    path("accounts/login/",views.logina, name='app'),
    path("logout",views.signout, name='app'),
    path("login2",views.login2, name='app'),
    path("register1",views.register1, name='app'),
    path("stud1",views.stud1, name='app'),
    path("stud/<int:id>",views.view, name='app'),
    path("vacant",views.vacant, name='app'),
    path("complaints",views.complaints, name='app'),
    path("incharge1",views.incharge1, name='app'),
    path("login1op",views.res, name='app'),
    path("exp",views.exp, name='app'),
    path("register1in/", views.register_request, name='register1in'),
]
