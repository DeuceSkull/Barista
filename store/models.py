from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Category')
    image = models.ImageField(upload_to='categories/', null=True, blank=True, verbose_name='Photo')
    slug = models.SlugField(unique=True, null=True)  # Dublikat qilib beradi
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               null=True, blank=True,
                               verbose_name='Category',
                               related_name='subcategories')

    def get_absolute_url(self):
        pass

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'Category: pk={self.pk}, title={self.title}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='Name of product')
    price = models.FloatField(verbose_name='Price')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Create')
    quantity = models.IntegerField(default=0, verbose_name='Count')
    description = models.TextField(default='Soon...', verbose_name='Description')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category', related_name='products')
    slug = models.SlugField(unique=True, null=True)

    def get_absolute_url(self):
        pass

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'Product: pk={self.pk}, title={self.title}, price={self.price}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Gallery(models.Model):
    image = models.ImageField(upload_to='products/', verbose_name='Photos')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'Picture'
        verbose_name_plural = 'Pictures'
