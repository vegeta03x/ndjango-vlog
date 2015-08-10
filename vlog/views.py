from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .form import PostForm
# Create your views here.

def post_list(request):
	posts = Post.objects.order_by('published_date')
	return render(request, 'vlog/post_list.html', {'posts' : posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'vlog/post_detail.html', {'post' : post})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('vlog.views.post_detail', pk=post.pk)	
	else:
		form = PostForm()
	return render(request, 'vlog/post_edit.html', {'form' : form})
