# -*- coding: utf-8 -*-

from __future__ import unicode_literals

#from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import redirect
from datetime import datetime
from .models import Post

# Create your views here.
def homepage(request):
	template = get_template('index.html')
	posts = Post.objects.all()
	now = datetime.now()
	#post_lists = list()
	html = template.render(locals())
	#for count, post in enumerate(posts):
	#	post_lists.append("No.{}".format(count) + post.title + "<hr>")
	#	post_lists.append("<small>" + post.body + "</small><br><br>")
	
	#return HttpResponse(post_lists)
	return HttpResponse(html)

def showpost(request, slug):
	template = get_template('post.html')
	try:
		post = Post.objects.get(slug=slug)
		if post != None:
			html = template.render(locals())
			return HttpResponse(html)
	except:
		return redirect('/')