from typing import NoReturn
from django.shortcuts import render, redirect
from .models import Category, Photo

def gallery(request):
    # category = request.GET('category')

    # print('category:',category)
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {'categories':categories, 'photos':photos}
    return render(request, 'app/gallery.html', context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    context = {'photo':photo}
    return render(request, 'app/photo.html', context)

def addPhoto(request):
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data ['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        photo = Photo.objects.create(
            category = category,
            description = data['description'],
            image=image,
        )

        return redirect('gallery')

        # test for submission on terminal
        # print('data:', data )
        # print('image:', image )
    categories = Category.objects.all()
    context = {'categories':categories,}
    return render(request, 'app/add.html', context)
