from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('login/', views.loginpage, name='loginpage'),
    path('profile/', views.profile, name='profile'),
    path('save_profile/<int:pk>/', views.save_profile, name='save_profile'),
    path('create_userinfo/<int:pk>/', views.create_userinfo, name='create_userinfo'),
    path('staff-profile/', views.staff_profile, name='staff_profile'),
    path('logout/', views.logout_view, name='logout'),
    # path('signup/', views.signup, name='signup'),
    url(r'^password/$', views.change_password, name='change_password'),
    path('add_member/', views.add_member, name='add_member'),
    path('popup/', views.popup, name='popup'),
    path('img_download/<int:year>/<int:sem>/', views.img_download, name='img_download'),
    path('img_download_page/', views.img_download_page, name='img_download_page'),
    path('user_check/', views.user_check, name='user_check'),
    path('no_student_id/<int:pk>/', views.no_student_id, name='no_student_id'),
    path('delete_userinfo/', views.delete_userinfo, name='delete_userinfo'),
    path('delete_userinfo_confirm/<int:year>/<int:sem>/<int:group_no>/', views.delete_userinfo_confirm, name='delete_userinfo_confirm'),
    # Added by CS
    path('example/', views.example, name='example'),
]
