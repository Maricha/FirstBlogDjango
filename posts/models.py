from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

def upload_location(instance, filename):
	return "%s/%s" %(instance.id, filename)

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=120)
	image = models.FileField(upload_to=upload_location, null=True, blank=True)
	content = models.TextField()
	update = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"id": self.id})