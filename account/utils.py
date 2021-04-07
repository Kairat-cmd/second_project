from django.db import models

class User():
    name = models.CharField(max_length=150)