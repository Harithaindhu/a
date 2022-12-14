from email.mime import image
from django.db import models

# Create your models here.
class register(models.Model):
    name=models.CharField(max_length=70,blank=False,null=False)
    position=models.CharField(max_length=70,blank=False,null=False)
    restaurant=models.CharField(max_length=100,blank=False,null=False)
    address=models.CharField(max_length=170,blank=False)
    phone_no=models.BigIntegerField()
    password=models.CharField(max_length=70,blank=False)

class items(models.Model):
    category=models.CharField(max_length=100,blank=False)
    name=models.CharField(max_length=100,blank=False)
    price=models.IntegerField()
    image=models.ImageField(upload_to='image',default=None)
    restaurant=models.CharField(max_length=100,blank=False)

class customer_details(models.Model):
    name=models.CharField(max_length=100,blank=False)
    address=models.CharField(max_length=200,blank=False)
    phone_no=models.BigIntegerField()
    item=models.CharField(max_length=100,blank=False)
    quantity=models.IntegerField()
    price=models.IntegerField()

class msg(models.Model):
    name=models.CharField(max_length=100,blank=False)
    job=models.CharField(max_length=100,blank=False)
    img=models.ImageField(upload_to='images',default=None)
    msg1=models.CharField(max_length=300,blank=False)
    

class restaurant(models.Model):
    name=models.CharField(max_length=100,blank=False)
    location=models.CharField(max_length=100,blank=False)
    address=models.CharField(max_length=200,blank=False)
    ph_no=models.BigIntegerField()
    email=models.EmailField()