from django.db import models


# Create your models here.

class Product(models.Model):  # new
    title = models.CharField(max_length=50)

    def __str__(self):  # new
        return self.title


