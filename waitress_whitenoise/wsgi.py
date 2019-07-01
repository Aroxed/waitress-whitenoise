"""
WSGI config for waitress_whitenoise project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'waitress_whitenoise.settings')

application = get_wsgi_application()

from waitress import serve

serve(application, listen='*:8080')
