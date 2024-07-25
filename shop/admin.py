from django.contrib import admin
from .models import *

# class categoryadmin(admin.ModelAdmin):
#     list_display=('name','img','description')


admin.site.register(Category)
admin.site.register(Products)
