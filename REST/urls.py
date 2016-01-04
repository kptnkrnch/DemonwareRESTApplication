from django.conf.urls import url
from REST import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	url(r'^REST/$', views.retrieveOrCreate),
	url(r'^REST/(?P<pk>[0-9]+)/$', views.retrieveUpdateOrDelete),
]

urlpatterns = format_suffix_patterns(urlpatterns)
