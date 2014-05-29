from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'plastic.app.views.home', name='home'),
    url(r'^admin/auth/user/$', 'plastic.app.views.user', name='user'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^signup/$', 'plastic.app.views.signup', name='signup'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout',
        kwargs={'next_page': '/'}),
)
urlpatterns += staticfiles_urlpatterns()
