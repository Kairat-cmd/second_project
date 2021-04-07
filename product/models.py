from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, primary_key=True)

    def __str__(self):
        return self.name


# on_delete=models.Cascade -  delete all what it has
# on_delete=models.Protect - it will not allow  you to delete if category has products
# on_delete=models.Restricted - it will not allow  you to delete if category has products
# on_delete=models.Set_null -  will be null
# on_delete=models.Set_default - will be changed to default
# on_delete=models.Do_nothing - will not do anything, recommended not to use


# we can skip about primary key, it creates by itself

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')


    def __str__(self):
        return self.title




# "ORM - (Object-Relational Mapping)" it is technology that links class with DB:


