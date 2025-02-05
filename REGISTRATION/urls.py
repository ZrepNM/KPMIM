from django.contrib import admin
from django.urls import path
from REGISTRATION import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('course/', views.course, name='course'),
    path('mentor/', views.mentor, name='mentor'),
    path('search/', views.search, name='search'),
    path('course/update_course/<str:c_code>', views.update_course, name='update_course'), 
]
