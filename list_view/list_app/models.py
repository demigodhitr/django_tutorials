from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    pass

class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)


# Create your models here.
