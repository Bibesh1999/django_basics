from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Income(models.Model):
    title=models.CharField(max_length=100)
    description =models.TextField(null=True ,blank=True)
    rupees=models.FloatField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title