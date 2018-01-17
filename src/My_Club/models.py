from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    id_card = models.IntegerField(max_length=16)
    department = models.CharField(max_length=10)
    