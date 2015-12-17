from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from .models import Track
# Create your views here.
def index(request):
    track = Track.objects.all()
    return render(request, 'musixscore/index.html', {'track':track})