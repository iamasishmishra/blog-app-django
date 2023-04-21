from django.contrib import admin
from contactForm.models import contactForm

# Register your models here.
class serviceAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','message')
admin.site.register(contactForm,serviceAdmin)