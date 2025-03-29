from django.db import models

# Create your models here.
class Weather(models.Model):
    temp=models.IntegerField()
    temp_min=models.IntegerField()
    temp_max=models.IntegerField()
    pressure=models.IntegerField()
    humidity=models.IntegerField()
    clouds=models.TextField(max_length=40)
