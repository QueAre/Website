from django.http import request
from django.shortcuts import render


def index(request):
    return render(request, '../templates/index.html')

def story(request):
    return render(request, '../templates/story.html')

def team(request):
    return render(request, '../templates/team.html')
