from django.db import models
from django.conf import settings
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from django.contrib.auth.models import User


class Post(models.Model):
    slug = models.SlugField()
    name = models.CharField('Название', max_length=40)
    info = models.TextField('Описание', default="")
    price = models.IntegerField('Цена')
    tags = TaggableManager()

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.text


class Order(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='orders')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='username_name')
    quantity = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_date']
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"{self.post} - {self.quantity}"