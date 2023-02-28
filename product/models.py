from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=100)
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class Hashtag(models.Model):
    name = models.CharField(max_length=300)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
