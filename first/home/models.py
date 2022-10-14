from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
#makemigrations-create changes and store in a file
#migrate-apply the pending changes created by makemigrations

class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    password=models.CharField(max_length=15)
    phone=models.CharField(max_length=12)
    dsc=models.TextField()
    date=models.DateField()