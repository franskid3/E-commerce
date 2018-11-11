from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Post(models.Model):
    title = models.CharField(default='Phone, Elecronics.....', max_length=100)
    description = models.TextField(default='')
    price = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    date_posted = models.DateTimeField(default=timezone.now)
    images = models.ImageField(default='default.jpg', upload_to='market_pics')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
      return reverse('post-detail', kwargs={'pk': self.pk})


def save(self):
    super().save()

    img = Image.open(self.image.path)

    if img.height > 300 or img.width > 300:
        output_size = (300, 300)
        img.thumbnail(output_size)
        img.save(self.image.path)
