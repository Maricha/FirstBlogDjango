from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^create/$', "posts.views.post_create"),
    url(r'^(?P<id>\d+)/$', "posts.views.post_detail", name='detail'),
    url(r'^$', "posts.views.post_list", name='list'),
    url(r'^(?P<id>\d+)/edit/$', "posts.views.post_update", name='update'),
    url(r'^(?P<id>\d+)/delete/$', "posts.views.post_delete"),
]
