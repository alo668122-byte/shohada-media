from django.shortcuts import render
from .models import MediaFile, MediaCategory

def home(request):
    media_type = request.GET.get('type', 'all')
    category_id = request.GET.get('category', None)

    files = MediaFile.objects.all()

    if media_type != 'all':
        files = files.filter(media_type=media_type)

    if category_id:
        files = files.filter(category_id=category_id)

    categories = MediaCategory.objects.all()

    context = {
        'files': files,
        'categories': categories,
        'current_type': media_type,
    }
    return render(request, 'media_app/home.html', context)