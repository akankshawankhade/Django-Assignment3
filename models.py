from django.db import models

# Create your models here.
class Student(models.Model):
    username=models.CharField(max_length=45)
    password=models.CharField(max_length=45)
    phone_no=models.CharField(max_length=10)
    address=models.CharField(max_length=45)