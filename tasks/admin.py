from django.contrib import admin
from .models import Task

# Esta clase ereda del modelo admin para asi poder ver los campos de solo lectura en el panel del administrador
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created', )

# Register your models here.
admin.site.register(Task, TaskAdmin)