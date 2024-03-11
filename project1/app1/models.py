from django.db import models
dep=[('IT','IT'),('FINANCE','FINANCE')]
class Employee(models.Model):
    eid=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=30)
    add=models.CharField(max_length=50)
    email=models.EmailField()
    dept=models.CharField(max_length=50,choices=dep)