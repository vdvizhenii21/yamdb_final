
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Categories, Genres, Reviews, Titles, User

admin.site.register(User, UserAdmin)
admin.site.register(Titles)
admin.site.register(Reviews)
admin.site.register(Categories)
admin.site.register(Genres)
