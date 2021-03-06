import os, sys

PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))

sys.path = [PROJECT_PATH, os.path.join(PROJECT_PATH, "../"), os.path.join(PROJECT_PATH, "../python-packages/")] + sys.path

from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'kalite.settings'
application = WSGIHandler()
