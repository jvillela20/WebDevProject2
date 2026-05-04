from django.contrib import admin
from .models import (
    Slider, MovieTheater, MovieTV, Advertisement,
    SocialLink, Celebrity, Trailer, TrailerItem, News, Tweet
)

admin.site.register(Slider)
admin.site.register(MovieTheater)
admin.site.register(MovieTV)
admin.site.register(Advertisement)
admin.site.register(SocialLink)
admin.site.register(Celebrity)
admin.site.register(Trailer)
admin.site.register(TrailerItem)
admin.site.register(News)
admin.site.register(Tweet)
