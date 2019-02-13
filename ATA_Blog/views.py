from django.shortcuts import render
from .models import Blog

# Create your views here.
def pageblog(request):
    blog = Blog.objects.all()
    return render(request, 'blogpage/blog.html', {'blog':blog})