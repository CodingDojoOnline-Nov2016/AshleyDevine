from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^profile$', views.profile),
    url(r'^profile/(?P<id>\d+)/delete$', views.delete, name = 'my_delete'),
    url(r'^profile/(?P<id>\d+)/update$', views.update, name = 'my_update'),
]
