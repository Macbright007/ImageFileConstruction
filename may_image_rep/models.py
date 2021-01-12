from django.db import models

# Create your models here.
class image(models.Model):
    title = models.CharField(max_length=50)
    tag = models.TextField()
    make = models.CharField(max_length=30)
    img = models.FilePathField(path='/img')
    