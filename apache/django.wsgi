import os
import sys

sys.path.append('/home/django')
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_logistics.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()

