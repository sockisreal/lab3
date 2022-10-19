from django.db import models

class Category(models.Model):
    name = models.CharField('Название категории', max_length=250)

class Product(models.Model):
    product_name = models.CharField('Название', max_length=250)
    price = models.IntegerField('Цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория товара')