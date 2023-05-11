from django.db import models

class Login(models.Model):
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=120)

class Meta:
    fields='__all__'

