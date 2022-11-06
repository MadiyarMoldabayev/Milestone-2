from pyexpat import model
from statistics import mode
from django.db import models

class EmpModel(models.Model):
    empname = models.CharField(max_length=100)
   
    
    dateofbirth = models.DateField(max_length = 100)
    iin = models.IntegerField()
    contact = models.IntegerField()
    departmentid = models.CharField(max_length=100)
    specializationid = models.CharField(max_length=100)
    experience = models.IntegerField()
    photo = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.IntegerField()
    schedule = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    rating = models.IntegerField()
    address = models.CharField(max_length=100)

  


    class Meta:
        db_table = "employee"

class Patient(models.Model):
    dateofbirth = models.DateField(max_length = 100)
    iin = models.IntegerField()
    fullname = models.CharField(max_length = 100)
    bloodgroup = models.CharField(max_length = 100)
    emergency_number = models.IntegerField()
    contact = models.IntegerField()
    address = models.CharField(max_length = 100)
    marital = models.CharField(max_length = 100)
    registration = models.DateField(max_length =100)

    class Meta:
        db_table = "patient"

