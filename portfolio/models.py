from django.db import models

# Create your models here.

class Project(models.Model): 
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to='portfolio/media')
    url = models.URLField(blank=True)
    upload_date = models.DateField(auto_now_add=True)
