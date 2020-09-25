from django.db import models
from django.urls import reverse

class Widget(models.Model):
    item = models.CharField(max_length=50)

    def __str__(self):
        return self.item

    def get_absolute_url(self):
        return reverse('index')
