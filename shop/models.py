from django.db import models


class Category(models.Model):
    slug = models.SlugField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    slug = models.SlugField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    def get_image(self):
        if self.images.exists():
            return self.images.first().image.url
        return "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQ1ipeQbFseUM_GzxwMoQj45w9HtAnu4eu5w&s"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="products/")


