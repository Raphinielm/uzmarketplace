from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=255)
    stock = models.IntegerField()
    price = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    discount = models.FloatField()
    description = models.CharField(max_length=255)
# Create your models here.
