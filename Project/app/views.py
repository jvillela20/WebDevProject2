from django.shortcuts import render, redirect
from django.contrib import messages
from .models import (
    Slider, MovieTheater, MovieTV, Advertisement,
    SocialLink, Celebrity, Trailer, TrailerItem, News, Tweet
)


def index(request):
    context = {
        'sliders':        Slider.objects.all(),
        'movies_theater': MovieTheater.objects.all(),
        'movies_tv':      MovieTV.objects.all(),
        'ads':            Advertisement.objects.all(),
        'social_links':   SocialLink.objects.all(),
        'celebrities':    Celebrity.objects.all(),
        'trailers':       Trailer.objects.all(),
        'trailer_items':  TrailerItem.objects.all(),
        'news_items':     News.objects.all(),
        'tweets':         Tweet.objects.all(),
    }
    return render(request, 'base.html', context)


def newsletter(request):
    # TODO: handle newsletter form POST
    if request.method == 'POST':
        email = request.POST.get('email', '')
        # process email subscription here
        messages.success(request, 'Subscribed successfully!')
        return redirect('index')
    return redirect('index')
