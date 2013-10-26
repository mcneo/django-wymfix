from django.conf.urls import patterns, url

from wymfix import views

urlpatterns = patterns('',
    url(r'^skin.js', views.js),
    url(r'^skin.css/icons.png', views.icons),
    url(r'^icons.png', views.icons),
    url(r'^skin.css', views.css),
    url(r'^wymiframe.css', views.wymiframecss),
    url(r'^proxy.html', views.proxy)
)