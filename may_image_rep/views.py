from django.shortcuts import render
from may_image_rep.models import image

# Create your views here.

#view for home page
def index(request):
    images = image.objects.all()
    context =  {
        'images': images
    }
    return render(request, 'index.html', context)

#view for info page
def detail(request, pk):
    img_info = image.objects.get(pk=pk)
    context = {
        'img_info': img_info
    }
    return render(request, 'detail.html', context)