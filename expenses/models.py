from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Expenses (models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(null=True,blank=True)
    bill=models.ImageField(upload_to='expenses/')
    rupees=models.FloatField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title     