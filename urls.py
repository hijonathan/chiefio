from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib.auth.forms import AuthenticationForm

import designsnapper.views as views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('designsnapper.urls')),
    (r'^dashboard/$', views.DashboardView.as_view()),
    (r'^manage/$', views.ManageView.as_view()),
    (r'^page/$', views.PageView.as_view()),
    (r'^example-framed-content/$', views.FramedContentView.as_view()),
    (r'^add/$', views.AddPageView.as_view()),
    (r'^debug/$', views.DebugView.as_view()),

    (r'^accounts/create/$', 'designsnapper.views.create_new_user'),
    (r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'authentication_form': AuthenticationForm,
        'template_name': 'app/login.html'}),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/designsnapper/'}),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls))
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
