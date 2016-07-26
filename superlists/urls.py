from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    # Examples:
    url(r'^$', 'blog.views.home_page', name='home'),
    url(r'^lists/', include('lists.urls')),
    url(r'^blog/', include('blog.urls', namespace='blog', app_name='blog')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
