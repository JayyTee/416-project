from django.db import models
from django.contrib.auth.models import User


class Favorites(models.Model):
    Title = models.CharField(max_length=200)  # movie title
    account = models.ForeignKey(User, on_delete=models.CASCADE)  # user
    link = models.CharField(max_length=200)  # link to youtube or google search
    description = models.CharField(max_length=400)
