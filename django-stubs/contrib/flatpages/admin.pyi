from django.contrib import admin as admin
from typing import Any

class FlatPageAdmin(admin.ModelAdmin):
    form: Any = ...
    fieldsets: Any = ...
    list_display: Any = ...
    list_filter: Any = ...
    search_fields: Any = ...
