from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

class Director(models.Model):
    name = models.CharField(max_length=100)
    movie = models.ManyToManyField(Movie, related_name='directors')