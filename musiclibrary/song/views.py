from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def artist(request):
    artist_list = Artist.objects.all()
    print(artist_list)
    context = {'artistList': artist_list}
    return render(request, 'song/artist.html', context)