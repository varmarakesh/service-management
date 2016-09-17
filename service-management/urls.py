from django.conf.urls import url
from django.contrib import admin
from views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ps/$', DetailView.as_view(), name = 'detailview'),
    url(r'^ps/(?P<filter>\w+)', DetailView.as_view(), name = 'detailview'),
]
