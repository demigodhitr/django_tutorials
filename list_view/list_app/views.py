from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import *
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login, authenticate, logout
from django.db import IntegrityError
import requests
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
import random
from decimal import Decimal
from django.core.mail import EmailMultiAlternatives, get_connection
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from datetime import datetime


def home(request):
    news = News.objects.all().order_by('-date_posted')
    return render(request, 'index.html', {'news': news})

def overview(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'overview.html', {'news': news})





# Create your views here.
