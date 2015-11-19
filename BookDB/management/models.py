from django.db import models

# Create your models here.

class Author(models.Model):
	# Author {AuthorID (PK), Name, Age, Country}
	AuthorID = models.IntegerField(primary_key=True)
	Name = models.CharField(max_length=30)
	Age = models.IntegerField()
	Country = models.CharField(max_length=30)

class Book(models.Model):
	# Book {ISBN (PK), Title, AuthorID (FK), Publisher, PublishDate, Price}
	ISBN = models.IntegerField(primary_key=True)
	Title = models.CharField(max_length=100)
	AuthorID = models.IntegerField()
	Publisher = models.CharField(max_length=60)
	PublishDate = models.IntegerField()
	Price = models.IntegerField()