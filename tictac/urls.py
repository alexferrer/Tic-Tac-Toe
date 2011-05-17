from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^hello$', 'tictac.mainapp.views.hello'),

    url(r'^board$', 'tictac.mainapp.views.paint_board'),
     
    url(r'^your_move$', 'tictac.mainapp.views.process_move'),    
    
    
    # url(r'^tictac/', include('tictac.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
