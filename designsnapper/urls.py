from django.conf.urls.defaults import patterns
from django.views.generic.simple import direct_to_template

import designsnapper.views as views


urlpatterns = patterns('',
    (r'^$', direct_to_template, {'template': 'marketing/index.html'}),

    (r'^platform/$', direct_to_template, {'template': 'marketing/platform.html'}),
    (r'^algorithms/$', direct_to_template, {'template': 'marketing/platform-algorithms.html'}),
    (r'^analysis/$', direct_to_template, {'template': 'marketing/platform-analysis.html'}),
    (r'^notifications/$', direct_to_template, {'template': 'marketing/platform-notifications.html'}),
    (r'^details/$', direct_to_template, {'template': 'marketing/platform-details.html'}),

    (r'^demo/$', views.DemoAddPageView.as_view()),

    (r'^pricing/$', direct_to_template, {'template': 'marketing/pricing.html'})
)
