from django.db import models
from django.urls import reverse 

#reverse is a useful function that allows us to reference an object by its URL template name recall our URL Pattern



class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
            'auth.User',
            on_delete=models.CASCADE,
    )
    body=models.TextField()


    def __str__(self):
        return self.title


    #get_absolute_url sets a URL to the objct that doesn't change

    def get_absolute_url(self):
        return reverse ('post_detail', args=[str(self.id)])
    # Create your models here.
