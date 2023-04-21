from django.http import HttpResponse
from django.shortcuts import render
from contactForm.models import contactForm
from blog.models import Post, Category
# from django.contrib import messages


# Create your views here.
def home(request):
    # post from database
    posts = Post.objects.all()[:11]
    # print(posts)
    cats = Category.objects.all()
    data = {
        'posts': posts,
        'cats': cats
    }
    return render(request, 'home.html', data)


def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()

    print(post)
    return render(request, 'posts.html', {'post': post, 'cats': cats})


def category(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, "category.html", {'cat': cat, 'posts': posts})

def contactUs(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        savedata = contactForm(name=name,email=email,phone=phone,message=message)
        savedata.save()
    return render(request, "contactUs.html",)

def about(request):
    return render(request, "about.html")