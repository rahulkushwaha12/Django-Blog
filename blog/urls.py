from django.conf.urls import patterns, url
from . import views, feed

urlpatterns = patterns(
	'blog.views',
	
	url(r'^search/', 'search'),
	url(r'^forum/', 'forum'),
	url(r'^opc-calender/', 'calender'),
	url(r'^about/', 'about'),
	url(r'^feed/$', feed.LatestPosts(), name="feed"),
    url(r'^$', views.BlogIndex.as_view(), name="index"),
    url(r'^(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
)
#urlpatterns = patterns('blog.views',
#    url(r'^about/', 'about'),
#)
