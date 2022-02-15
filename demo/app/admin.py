from django.contrib import admin

from . models import Feedback



class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'city', 'status')

admin.site.register(Feedback, FeedbackAdmin)