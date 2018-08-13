from django.db import models

# Create your models here.
from django.db import models

class Office(models.Model):
    Product_Name = models.CharField(max_length=250)
    License_Keys = models.CharField(max_length=250)
    Machine_ID = models.CharField(max_length=250)
    Machine_Type = models.CharField(max_length=250)
    Asset_Number = models.CharField(max_length=250)
    User = models.CharField(max_length=250)
    Notes_1 = models.CharField(max_length=250)
    Notes_2 = models.CharField(max_length=250)
    Notes_3 = models.CharField(max_length=250)


    def __str__(self):
        return self.Product_Name + ' - ' + self.License_Keys + ' - ' + self.User + ' - ' + self.Notes_1 + ' - ' + self.Notes_2

class Other(models.Model):
    Product = models.CharField(max_length=250)
    Product_Key = models.CharField(max_length=250)
    Machine_ID = models.CharField(max_length=250)
    Machine_Type = models.CharField(max_length=250)
    Asset_Number = models.CharField(max_length=250)
    User = models.CharField(max_length=250)
    Purchase_Date = models.CharField(max_length=250)
    Notes = models.CharField(max_length=250)

    def __str__(self):
        return self.Product + ' - ' + self.Product_Key + ' - ' + self.User