from django.db import models
from .category import Category

class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    category=models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    description=models.CharField(max_length=50000,default='',blank=True,null=True)
    image=models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name