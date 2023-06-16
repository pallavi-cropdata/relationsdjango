from django.contrib import admin
from . models import Interest,City,Person,PersonAddress

# Register your models here.
admin.site.register(Interest)
admin.site.register(City)
admin.site.register(Person)
admin.site.register(PersonAddress)


