from django.db import models


class Genre(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
	
class Performer(models.Model):
	name = models.CharField(max_length=50)
	genre_id = models.ManyToManyField(Genre, null=True, blank=True)
	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
		
class Album(models.Model):
	name = models.CharField(max_length=50)
	performer_id = models.ForeignKey(Performer, null=True, blank=True)
	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
	
class Track(models.Model):
	name = models.CharField(max_length=50)
	album_id = models.ForeignKey(Album, null=True, blank=True)
	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
