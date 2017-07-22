from django.conf.urls import url

from . import views

app_name = 'cdemo'

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^login/$', views.login_result, name='login_result'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^index/$', views.main, name='main'),
    url(r'^project/$', views.cproject, name='cproject'),
    url(r'^project_create/$', views.ccreate_project, name='cproject_create'),
    url(r'^config_test/$', views.cconfig_test, name='cconfig_test'),
    url(r'^test_add_content/$', views.test_cconfig_content_add, name='test_add_content'),
]



