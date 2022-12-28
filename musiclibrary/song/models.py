from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=250)
    country = models.CharField(max_length=50)
    birth_year = models.IntegerField()
    genre = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name
    
class Song(models.Model):
    title = models.CharField(max_length=250)
    release_date = models.DateField()
    length = models.IntegerField()
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)