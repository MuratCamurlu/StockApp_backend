from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=25,unique=True)
    image=models.TextField()
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=100,unique=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,related_name="b_products")
    stock=models.SmallIntegerField(blank=True,default=0)