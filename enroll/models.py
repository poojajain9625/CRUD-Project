from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=70)
    email=models.CharField(max_length=100, unique=True, error_messages={'unique': 'E-Mail id must be unique.'})
    password=models.CharField(max_length=100)