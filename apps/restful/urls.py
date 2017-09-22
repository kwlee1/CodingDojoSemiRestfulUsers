from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^users/$',views.index),
    url(r'^users/new',views.new),
    url(r'^users/create',views.create),
    url(r'^users/(?P<id>[0-9]{1,})$',views.show,name='show'),
    url(r'^users/(?P<id>[0-9]{1,})/delete$',views.delete,name='delete'),
    url(r'^users/(?P<id>[0-9]{1,})/edit$',views.edit,name='edit'),
    url(r'^users/(?P<id>[0-9]{1,})/update$',views.update,name='update')
]
