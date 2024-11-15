from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    address=models.TextField()
    email=models.EmailField()
    image=models.ImageField(upload_to="images")
