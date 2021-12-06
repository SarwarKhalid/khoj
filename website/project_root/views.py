import os

from django.shortcuts import render, redirect
from django.db import connection, connections

from django.core.exceptions import ObjectDoesNotExist

from auth_app import *

from django.http import  HttpResponse

def index(request):

    if request.user.is_authenticated:
        params = {'msg_cluster': 'Here are your clusters'}
        print("if part execute")
        return render(request, 'index.html', params)
    else:
        print("else part execute")
        params = {'msg_cluster': 'login to view clusters'}
        return render(request, 'index.html', params)


