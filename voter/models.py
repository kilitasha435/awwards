from django.db import models
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile' )
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return f'{self.user.username} Pofile'


class Post(models.Model):
    title = models.CharField(max_length=150)
    url = models. CharField(max_length=255)
    description = models.TextField(max_length=500)
    technologies = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.title}'
