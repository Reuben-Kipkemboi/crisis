from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from .forms import *
from django.contrib.auth.decorators import login_required

# APPLICATION VIEWS.
# home function
def home(request):
    return render(request, 'crisis/index.html')

