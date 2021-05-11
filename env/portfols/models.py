from django.db import models

# Create your models here.

class Service(models.Model):
    images= models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.summary


class Projects(models.Model):
    images= models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=20)
    imageurl = models.CharField(max_length = 80, default="notjustok")

    def __str__(self):
        return self.summary
