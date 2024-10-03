from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    description = models.TextField()
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.title