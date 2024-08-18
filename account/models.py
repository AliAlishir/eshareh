from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    phone_number = models.CharField(max_length=13, verbose_name="شماره تلفن")
    avatar = models.ImageField(upload_to='images/user')