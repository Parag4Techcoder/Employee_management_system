from django.contrib import admin
from mirai.models import Company,Employee


# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('cName','cEmail','cLocation','cLogo','cUrl')
admin.site.register(Company,CompanyAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('eFname','eLname','eCompany','eEmail','ePhone')
admin.site.register(Employee,EmployeeAdmin)