from django.http import HttpResponse
import urllib2
import mimetypes

from django.conf import settings
STATIC_URL = getattr(settings, 'STATIC_URL', '')


def css(request):
    url = '%scms/js/wymeditor/skins/django/skin.css' % STATIC_URL
    return _proxy(url)


def js(request):
    url = '%scms/js/wymeditor/skins/django/skin.js' % STATIC_URL
    return _proxy(url)


def icons(request):
    url = '%scms/js/wymeditor/skins/django/icons.png' % STATIC_URL
    return _proxy(url)


def wymiframecss(request):
    url = '%scms/wymeditor/iframe/default/wymiframe.css' % STATIC_URL
    return _proxy(url)


def proxy(request):

    url = STATIC_URL
    url += request.META.get('QUERY_STRING')

    return _proxy(url)


def _proxy(url):
    try:
        proxied_request = urllib2.urlopen(url)
        status_code = proxied_request.code
        mimetype = proxied_request.headers.typeheader or mimetypes.guess_type(url)
        content = proxied_request.read()
    except urllib2.HTTPError as e:
        msg = e.msg + ' : ' + url
        return HttpResponse(msg, status=e.code, mimetype='text/plain')
    else:
        return HttpResponse(content, status=status_code, mimetype=mimetype)