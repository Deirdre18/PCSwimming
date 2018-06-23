# LOCAL SETTINGS
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vj#j6)5#b^sr9t3#2zmy**0@a25(z4s7_u^6j@8&8j5##=_vsi'

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')