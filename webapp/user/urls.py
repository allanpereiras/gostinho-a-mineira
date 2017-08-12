from user.forms import LoginForm

from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^login/$', auth_views.login,
        {'template_name': 'user/login.html',
         'authentication_form': LoginForm}, name='Login'),
    # url(r'^logout/$',
    #     views.user_logout, name='Logout'),
    # url(r'^new/$', views.registrate, name='Registrate'),
    # url(r'^profile/$',
    #     views.user_profile, name='Profile'),
    # url(r'^updatepassoword/$',
    #     views.user_update_password, name='Update_password'),
]
