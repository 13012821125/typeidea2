from .base import *  # NOQA
"""上面那个注释是告诉PEP8，这个地方不需要检测"""
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
