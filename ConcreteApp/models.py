from django.db import models
from django.forms import model_to_dict

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name
