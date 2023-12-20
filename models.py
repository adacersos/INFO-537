from django.db import models

class Student1 (models.Model):
    STID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=200)

