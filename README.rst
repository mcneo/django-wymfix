=====
wymfix
=====

Want to use Django CMS and use S3 for your static files; then you'll need a fix for the Wymeditor,
otherwise it'll complain about Cross Site Scripting! Get your fix here!

Quick start
-----------

1. Add "wymfix" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'wymfix',
    )

2. Include the wymfix URLconf in your project urls.py like this::

    url(r'^wymfix/', include('wymfix.urls')),