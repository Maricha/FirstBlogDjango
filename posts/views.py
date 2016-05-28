from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post
# Create your views here.

def post_create(request):
	return HttpResponse("hello")

def post_detail(request, id=None):
	instance = get_object_or_404(Post, id=id)
	context = {
		"title": instance.title,
		"instance": instance,
	}
	return render(request, "post_detail.html", context)

def post_list(request):
	# if request.user.is_authenticated():
	# 	context = {
	# 		"title": "My User List"
	# 	}
	# else:
	# 	context = {
	# 		"title": "List"
	# 	}

	queryset = Post.objects.all();
	context = {
		"object_list" : queryset,
		"title": "List",
	}
	
	return render(request, "index.html", context)

def post_update(request):
	return HttpResponse("hello")

def post_delete(request):
	return HttpResponse("hello")