from django.db import models

# Create your models here.
class Country(models.Model):
    country_id=models.IntegerField(primary_key=True)
    country_name=models.CharField(max_length=100)

class Capital(models.Model):
    capital_id=models.IntegerField(primary_key=True)
    capital_name=models.CharField(max_length=100)
    country_id=models.OneToOneField(Country,on_delete=models.CASCADE)    

    
