++++++++++++++++++++++++++++++
from django.contrib import admin
from Multiple_App.models import Bank,Loan,Employee,Customer

class BankAdmin(admin.ModelAdmin):
    list_display = ['bank_id','bank_name','address','ifsc']

class LoanAdmin(admin.ModelAdmin):
    list_display = ['loan_id','loan_type']

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['emp_name','account_number']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_name','account_number']

admin.site.register(Bank,BankAdmin)
admin.site.register(Loan,LoanAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Customer,CustomerAdmin)
