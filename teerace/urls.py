from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^$', 'django.views.generic.simple.direct_to_template',
		{'template': 'home.html'}, name='home'),
	(r'^user/', include('accounts.urls')),
)
