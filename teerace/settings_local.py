"""
settings_local.py

Change site-specific settings here.
"""

from settings_default import *

"""
There's a list of settings that you will probably override.
"""

"""
DEBUG

Turns Django into development mode.

Default: False
"""
#DEBUG = False

"""
TEMPLATE_DEBUG

Additional debug data for templates.

Default: False
"""
#TEMPLATE_DEBUG = False

"""
TEMPLATE_CACHING

Specifies whether templates should be cached or not.

Default: True
"""
#TEMPLATE_CACHING = True

"""
INTERNAL_IPS

Used by django-debug-toolbar.

Default: ('127.0.0.1',)
"""
#INTERNAL_IPS = ('127.0.0.1',)

"""
ADMINS

A list of chaps maintaining the app.

Default: ()
"""
#ADMINS = (
#	('John Doe', 'joe@doe.com'),
#)

"""
DATABASES

Database-stuff.

Default: SQLite database
"""
#DATABASES = {
#	'default': {
#		# Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3'.
#		'ENGINE': 'django.db.backends.sqlite3',
#		# Or path to database file if using sqlite3.
#		'NAME': PROJECT_DIR + '/teerace.sqlite',
#		# Not used with sqlite3.
#		'USER': '',
#		# Not used with sqlite3.
#		'PASSWORD': '',
#		# Set to empty string for localhost. Not used with sqlite3.
#		'HOST': '',
#		# Set to empty string for default. Not used with sqlite3.
#		'PORT': '',
#	}
#}

"""
CACHE_BACKEND

Default: cache will be stored in local RAM.
With memcached: 'johnny.backends.memcached://localhost:11211/'
"""
#CACHE_BACKEND = 'johnny.backends.locmem://'

"""
WEBMASTER_EMAIL

E-mail address displayed when 404/500 is raised.

Default: ""
"""
#WEBMASTER_EMAIL = ''

"""
RECAPTCHA_PUBLIC_KEY



Default: ""
"""
#RECAPTCHA_PUBLIC_KEY = ''

"""
RECAPTCHA_PRIVATE_KEY



Default: ""
"""
#RECAPTCHA_PRIVATE_KEY = ''


"""
SECRET_KEY

The Answer to the Ultimate Question of Life, the Universe, and Everything.

Default: "foobar" (PLEASE CHANGE THAT)
"""
#SECRET_KEY = 'foobar'

"""
BROKER_HOST

Hostname of the broker.
"""
#BROKER_HOST = "localhost"

"""
BROKER_PORT

Custom port of the broker.
Default is to use the default port for the selected backend.
"""
#BROKER_PORT = 5672

"""
BROKER_USER

Username to connect as.
"""
#BROKER_USER = "guest"

"""
BROKER_PASSWORD

Password to connect with.
"""
#BROKER_PASSWORD = "guest"

"""
MIDDLEWARE_CLASSES

You might want to add some debug stuff here.
"""
#MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + ()


"""
INSTALLED_APPS

You might want to add some debug stuff here.
"""
#INSTALLED_APPS = INSTALLED_APPS + ()
