from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register, name="register"),
    path('my-login', views.myLogin, name="my-login"),
    path('dashboard', views.dashboard, name='dashboard'),
    path('user-logout', views.useLogout, name='user-logout'),

    # CRUD
    path('create-record', views.create_record, name='create-record'),
    path('update-record/<int:pk>', views.update_record, name='update-record'),    #UPDATE
    path('record/<int:pk>', views.record, name='record'),    
    path('delete-record/<int:pk>', views.delete_record, name='delete-record'),    
]
