from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post, Category

def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    categories = find_active_categories()
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "posts": posts,
        'categories': categories,
        'page_obj':page_obj,
    }
    return render(request, "main_page/index.html", context)

# def categories_list(request, category):
#     posts = Post.objects.filter(categories__name__contains=category).distinct()
#     paginator = Paginator(posts, 9)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     categories = find_active_categories()

#     context = {
#         'page_obj': page_obj,
#         'categories': categories,
#     }
#     return render(request, 'main_page/index.html', context)

def find_active_categories():
    categories = [category for category in Category.objects.all() if len(category.posts.all()) > 0]
    return categories   

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    categories = find_active_categories()
    context = {
        "category": category,
        'categories': categories,
        "posts": posts,
    }
    return render(request, "main_page/category.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
            "post": post,
    
    }

    return render(request, "main_page/detail.html", context)
