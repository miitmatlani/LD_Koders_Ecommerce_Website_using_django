from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Contact(models.Model):
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return '{} , {}'.format(self.name , self.email)



class Profile(models.Model):
    appnauser = models.OneToOneField(User, on_delete=models.CASCADE)
    # bio = models.TextField(max_length=500, blank=True)
    ph_number = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=30, blank=True)
    Address_line_1= models.CharField(max_length=30, blank=True)
    Address_line_2 = models.CharField(max_length=30, blank=True)
    pincode = models.CharField(max_length=7, blank=True)
    country = models.CharField(max_length=30, blank=True)
    state_or_region = models.CharField(max_length=30, blank=True)
    # birth_date = models.DateField(null=True, blank=True)
    account_created_Date = models.DateField(null=True, blank=True)

    def __str__(self):
        return '{} , {}'.format(self.appnauser, self.location)

@receiver(post_save, sender=User)
def create_user_Profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(appnauser=instance)

@receiver(post_save, sender=User)
def save_user_Profile(sender, instance, **kwargs):
    instance.profile.save()


class Product_Details(models.Model):
    Index = models.IntegerField(primary_key=True)
    Product_Catagory = models.CharField(max_length=122)
    Product_Sub_Catagory = models.CharField(max_length=122)
    Product_Name = models.CharField(max_length=256)
    Brand = models.CharField(max_length=122)
    Retail_Price = models.IntegerField()
    Description = models.CharField(max_length=2546)
    Image_1 = models.CharField(max_length=256)
    Image_2 = models.CharField(max_length=256)
    Image_3 = models.CharField(max_length=256)

    def __str__(self):
        return self.Product_Name



class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_jason = models.CharField(max_length=5000)
    amount = models.IntegerField(default=40)
    fname_pay = models.CharField(max_length=122)
    lname_pay = models.CharField(max_length=122)
    email_pay = models.CharField(max_length=122)
    address_pay = models.CharField(max_length=122)
    city_pay = models.CharField(max_length=122)
    state_pay = models.CharField(max_length=122)
    zipcode_pay = models.CharField(max_length=122)
    phone_pay = models.CharField(max_length=122,default='0000000000')