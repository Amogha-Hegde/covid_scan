"""
Django settings for covid_scan project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$v!yua5#vtug_*5&ii2t7chl#4*o=o&23k49o$&@yb9j3w@o5-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'pages.apps.PagesConfig',
    'accounts.apps.AccountsConfig',
    'user_data.apps.UserDataConfig',
    'wkhtmltopdf',
    #"rest_framework_api_key"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'covid_scan.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'covid_scan.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

#----------------------------------------------
#Database Connecton from Google Cloud Platform
#-----------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Enter Your Database User', #Enter your Database name
        'USER': 'Enter Your Database User',   #Enter Your Database User
        'PASSWORD': 'Enter Database Password',    #Enter Database Password
        'HOST': 'Enter Public IP Address of  Cloud SQL instanc', #Enter Public IP Address of  Cloud SQL instance  
        'PORT': 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    
   os.path.join(BASE_DIR,'covid_scan/static')

]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



#GCP BUCKET INTEGRATION

from google.oauth2 import service_account

GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
   os.path.join(BASE_DIR,'credentials.json')
)

PROJECT_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
DEFAULT_FILE_STORAGE = 'covid_scan.gcloud.GoogleCloudMediaFileStorage'
#STATICFILES_STORAGE = 'gcloud.GoogleCloudStaticFileStorage'
GS_DEFAULT_ACL = None
GS_QUERYSTRING_AUTH = False  
GS_PROJECT_ID = 'GCP Projrct ID'          # Enter GCP Project ID
GS_STATIC_BUCKET_NAME = 'GCP BUCKET NAME' #Enter GCP BUCKET NAME
GS_MEDIA_BUCKET_NAME = 'GCP BUCKET NAME'  # same as STATIC BUCKET if using single bucket both for static and media

MEDIA_URL = 'https://storage.googleapis.com/{}/'.format(GS_MEDIA_BUCKET_NAME)
MEDIA_ROOT = "media/"    
UPLOAD_ROOT = 'media/uploads/' 
DOWNLOAD_ROOT = os.path.join(PROJECT_ROOT, "static/media/downloads")
DOWNLOAD_URL = STATIC_URL + "media/downloads"


#SMTP BACKEND
#If you are using gmail as SMTP Backend allow less secure apps in gmail settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'Email'          # Enter Your Email Address
EMAIL_HOST_PASSWORD = 'Password'   # Enter Password
EMAIL_PORT = 587

#If you want to use Twilio SMS Service Please Uncomment The code
'''
#Twilio SETUP
ACCOUNT_SID = "Account id" #Enter Twilio Account id
AUTH_TOKEN = "Auth Token"    #Enter Twilio Auth Token
'''

WKHTMLTOPDF_CMD_OPTIONS = {
    'quiet': True,
}