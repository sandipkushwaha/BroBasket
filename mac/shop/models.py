from django.db import models


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default=" ")
    subcategory = models.CharField(max_length=50, default=" ")
    price = models.IntegerField(default=0)
    disc = models.CharField(max_length=300, default="  ")
    prod_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default=" ")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70, default=" ")
    phone = models.CharField(max_length=70, default=" ")
    desc = models.CharField(max_length=500, default="  ")

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=90, default=" ")
    address = models.CharField(max_length=220, default=" ")
    city = models.CharField(max_length=100, default=" ")
    state = models.CharField(max_length=110, default="  ")
    zip_code = models.CharField(max_length=10, default="  ")
    phone = models.CharField(max_length=15, default="  ")


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default=" ")
    update_desc = models.CharField(max_length=500)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "....."
