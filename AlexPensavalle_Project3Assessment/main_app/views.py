
from django.shortcuts import render
from .models import Widget

def index(request):
    widgets = Widget.objects.all()
    return render(request, 'index.html', {'widgets': widgets})