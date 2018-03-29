from django.contrib import admin
from guardian.admin import GuardedModelAdmin

# Register your models here.
from .models import Item


@admin.register(Item)
class ItemAdmin(GuardedModelAdmin):

    class Meta:
        verbose_name = 'アイテム'
        verbose_name_plural = 'アイテム'
