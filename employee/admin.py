from django.contrib import admin
from employee.models import Employee,Attendance,Notice, SalaryDetail

# Register your models here.

# Register your models here.
admin.site.register(Employee)
admin.site.register(Attendance)
admin.site.register(Notice)


class SalaryDetailAdmin(admin.ModelAdmin):
    list_display = ('user', 'month', 'time', 'net_amount', 'credited','pending_amount', 'status')
    list_filter = ('month', 'status')
    search_fields = ('user__username', 'user__first_name', 'user__last_name')

admin.site.register(SalaryDetail, SalaryDetailAdmin)
