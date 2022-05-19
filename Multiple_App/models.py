
from django.db import models

class Bank(models.Model):
    bank_id = models.IntegerField(primary_key=True)
    bank_name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    ifsc = models.CharField(max_length=50, unique=True)

    def  __str__(self):
        return self.bank_name

class Loan(models.Model):
    loan_id = models.IntegerField(primary_key=True)
    loan_type = models.CharField(max_length=50)

    def  __str__(self):
        return self.loan_type


class Employee(Bank,Loan):
    emp_name  = models.CharField(max_length=30)
    account_number = models.IntegerField(unique=True)

    def __str__(self):
        return self.emp_name

class Customer(Bank,Loan):
    customer_name  = models.CharField(max_length=30)
    account_number = models.IntegerField(unique=True)

    def __str__(self):
        return self.customer_name


