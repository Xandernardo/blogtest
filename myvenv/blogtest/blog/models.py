from django.db import models
from django.utils import timezone

class Post(models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    create_date = models.DateTimeField(
        default=timezone.now)
    publish_date = models.DateTimeField(
        blank=True, null = True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    autor = models.CharField(max_length=200)
    contenido = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.contenido

# Create your models here.
