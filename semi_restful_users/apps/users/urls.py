from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.indexredirect),
    url(r'^users/$', views.index),
    url(r'^users/new/$', views.new),
    url(r'^users/new/create/$', views.create),
    url(r'^users/info/(?P<id>\d+)$', views.info),
    url(r'^users/edit/(?P<id>\d+)$', views.edit),
    url(r'^users/edit/(?P<id>\d+)/update/$', views.update),
    url(r'^users/delete/(?P<id>\d+)$', views.delete),
]
