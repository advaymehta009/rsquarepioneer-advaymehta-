from django.urls import path, include
from . import views
from  django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('signup/', views.register, name='signup'),
    path('addstudent/', views.add_student, name='addstudent'),
    path('viewstudent/', views.view_student, name='viewstudent'),
    path('drivers/', views.viewdriver, name='viewdrivers'),
    path('adddriver/', views.adddriver, name='adddriver'),
    path('conductors/', views.conductor, name='conductors'),
    path('addconductor/', views.addconductor, name='addconductor'),
    path('viewbuses/', views.bus, name='viewbus'),
    path('addbus/', views.addbus, name='addbus'),
    path('routes/', views.routes, name='routes'),
    path('addroute/', views.addroute, name='addroute'),
    path('owner/', views.owner, name='owners'),
    path('addowner/', views.addtheowner, name='addowner'),
    path('school/', views.school, name='school'),
    path('addschool/', views.addschool, name='addschool'),
    path('teacher/', views.teacher, name='teacher'),
    path('addteacher/', views.addteacher, name='addteacher'),
    path('manage-accounts/', views.manageaccounts, name='manageaccounts'),
    path('dash-signup/', views.signupdashboard, name='signupdashboard'),
    path('collectfee/', views.collectfee, name='collectfee'),
    path('invoice/<int:pk>/', views.invoice, name='invoice'),
    path('students/profile/<int:pk>', views.student_single, name='single-student'),
    path('teacher/profile/<int:pk>', views.teacher_single, name='single-teacher'),
    path('owners/profile/<int:pk>', views.owner_single, name='single-owner'),
    path('drivers/profile/<int:pk>', views.driver_single, name='single-driver'),
    path('conductor/profile/<int:pk>', views.conductor_single, name='single-conductor'),
    path('feecollector/profile/<int:pk>', views.feecollector_single, name='single-feecollector'),
    path('bus/profile/<int:pk>', views.bus_single, name='single-bus'),
    path('feecollector/', views.feecollector, name='feecollector'),
    path('addfeecollector/', views.addfeecollector, name='addfeecollector'),
    path('userprofile/<int:pk>', views.userprofile, name='userprofile'),
    path('routes/<int:pk>', views.singleroute, name='single-route'),
    path('addexpense/', views.add_expense, name='addexpense'),
    path('viewexpense/', views.view_expense, name='viewexpense'),

]