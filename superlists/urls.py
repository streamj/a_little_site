from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog.views.home_page', name='home'),
    url(r'^lists/', include('lists.urls')),
    url(r'^blog/', include('blog.urls')),
    # flat pages
    url(r'^blog/', include('django.contrib.flatpages.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
