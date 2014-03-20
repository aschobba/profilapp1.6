from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib.auth import views as auth_views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'profilapp.views.home', name='home'),
    # url(r'^profilapp/', include('profilapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', auth_views.login,
    {'template_name': 'registration/login.html'},
    name='auth_login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^addressbook/', include('addressbook.urls')),
    (r'^accounts/', include('registration.backends.default.urls')), 
    url(r'^password/change/$',
                    auth_views.password_change,
                    name='password_change'),
      url(r'^password/change/done/$',
                    auth_views.password_change_done,
                    name='password_change_done'),
      url(r'^password/reset/$',
                    auth_views.password_reset,
                    name='password_reset'),
      url(r'^password/reset/done/$',
                    auth_views.password_reset_done,
                    name='password_reset_done'),
      url(r'^password/reset/complete/$',
                    auth_views.password_reset_complete,
                    name='password_reset_complete'),
      url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
                    auth_views.password_reset_confirm,
                    name='password_reset_confirm'),
      (r'^facebook/', include('django_facebook.urls')),
)

urlpatterns += staticfiles_urlpatterns()
