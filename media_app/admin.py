from django.contrib import admin
from .models import MediaCategory, MediaFile

@admin.register(MediaCategory)
class MediaCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    list_display = ['title', 'media_type', 'category', 'created_at']
    list_filter = ['media_type', 'category', 'created_at']
    search_fields = ['title', 'description']