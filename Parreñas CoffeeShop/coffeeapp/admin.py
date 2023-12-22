# coffeeapp/admin.py

from django.contrib import admin
from django.contrib.admin.models import LogEntry

@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    actions = ['delete_selected']

    def delete_selected(self, request, queryset):
        queryset.delete()

    def has_delete_permission(self, request, obj=None):
        # Limit delete permission to superusers only
        return request.user.is_superuser

    delete_selected.short_description = "Delete selected recent actions"
