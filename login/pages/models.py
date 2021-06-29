from django.db import models

# Create your models here.

class UserDetails(models.Model):
     id = models.AutoField(primary_key = True)
     name = models.CharField(max_length = 100)
     email = models.EmailField()
     ph = models.CharField(max_length = 15)
