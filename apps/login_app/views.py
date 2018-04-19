# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
    return render(request, 'login_app/index.html')

def register(request):
    if User.userManager.isValidRegistration(request.POST, request):
        passFlag = True
        return redirect (reverse('success'))
    else:
        passFlag = False
        return redirect(reverse('index'))

def success(request):
    return render(request, 'login_app/success.html')

def login(request):
    if User.userManager.UserExistsLogin(request.POST, request):
        passFlag = True
        return redirect (reverse('success'))
    else:
        passFlag = False
        return redirect (reverse('index'))
