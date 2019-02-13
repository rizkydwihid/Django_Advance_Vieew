from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Blog
from .form import PostForm

# Create your views here.
def pageblog(request):
    blog = Blog.objects.all()
    return render(request, 'blogpage/blog.html', {'blog':blog})

def form(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_at = timezone.now()
            post.save()
            return redirect('blog')
    else:
        form = PostForm()
    return render(request, 'blogpage/form_page.html', {'form': form})

def detail_post(request, post_id):
    post_num = get_list_or_404(Blog, id=post_id)
    return render(request, 'blogpage/blog2.html', {'blog': post_num})