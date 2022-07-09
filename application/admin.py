from django.contrib import admin
from .models import User, Platform

#user_registering

@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ["platform_name", "conf"]

