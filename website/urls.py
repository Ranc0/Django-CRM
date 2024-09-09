from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name='home'),
    path('logout', views.logout_user , name='logout'),
    path('register', views.register_user , name='register'),
    path('record/<str:id>', views.record , name='record'),
    path('delete_record/<str:id>', views.delete_record , name='delete_record'),
    path('add_record', views.add_record , name='add_record'),
    path('update_record/<str:id>', views.update_record , name='update_record'),
]
