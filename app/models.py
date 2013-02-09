from django.db import models

from django.contrib.auth.models import User

class UserProfile(models.Model):
    """
    Extension of the basic Django User
    """
    user = models.OneToOneField(User)
    bio = models.CharField(max_length=255, blank=True, null=True, default="")

    def __unicode__(self):
        return "%s" % self.user

class Post(models.Model):
	"""
	Time to make a blog!
	"""
	author = models.ForeignKey(User)
	title = models.CharField(max_length=1000, null=False)
	text = models.CharField(max_length=20000, null=False)
	date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return "%s was written by %s on %s" % (self.title, self.author, self.date)

# Create your models here.
