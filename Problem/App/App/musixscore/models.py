from django.db import models


class Genre(models.Model):
	name = models.CharField()
	def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
	
class Performer(models.Model):
	name = models.CharField()
	genre_id = models.ManyToManyField(Genre, null=True, blank=True)
	def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
		
class Album(models.Model):
	name = models.CharField()
	def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
	
class Track(models.Model):
	name = models.CharField()
	def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
