from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BookDB.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'management.views.showHomepage_rdir'),
    url(r'^management/$', 'management.views.showHomepage'),
    url(r'^view_info/$', 'management.views.viewInfoPage'),
    url(r'^add_book/$', 'management.views.addBook'),
    url(r'^del/$', 'management.views.delete'),
)
