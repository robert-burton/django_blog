from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#Tablas para la BD
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #Asigna fecha actual cuando se crea objeto
    date_posted = models.DateTimeField(default=timezone.now)
    #Si un usuario se borra, se borran sus publicaciones
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
