from django.contrib import admin
from .models import PBSUser, Teacher, Student, Conductor, Driver, Owner, School

admin.site.register(School)
admin.site.register(PBSUser)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Conductor)
admin.site.register(Driver)
admin.site.register(Owner)
