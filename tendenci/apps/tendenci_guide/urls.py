from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('tendenci.apps.tendenci_guide.views',
    url(r'^guide/(?P<slug>[\w\-]+)/$', 'guide_page', name="tendenci_guide.guide_page"),
)

