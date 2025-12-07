import os
from pathlib import Path

# Import local settings
from .local_settings import (
    SECRET_KEY, DEBUG, ALLOWED_HOSTS, DB_CONFIG,
    TEMPLATES_DIR, STATICFILES_DIR, STATIC_DIR, MEDIA_DIR, LOGS_DIR,
    EMAIL_USER, EMAIL_PASSWORD, DEFAULT_EMAIL
)

# MAIN PROJECT BASE DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "Home"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "Garmen_textile.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATES_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "Garmen_textile.wsgi.application"

# Database
DATABASES = {
    "default": DB_CONFIG
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = "/static/"
STATIC_ROOT = STATIC_DIR               # Production
STATICFILES_DIRS = [STATICFILES_DIR]   # Development

# Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = MEDIA_DIR

# Email (Gmail)
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = EMAIL_USER
EMAIL_HOST_PASSWORD = EMAIL_PASSWORD
DEFAULT_FROM_EMAIL = DEFAULT_EMAIL

# -------------------------------------------------------------
# Logging Configuration
# -------------------------------------------------------------
# Turn off logging when running in CI/CD (Jenkins, Celery, automated builds)
# Example: export DISABLE_LOGGING=1

disable_log = os.getenv('DISABLE_LOGGING', '').lower() in ['1', 'true', 'yes']

if disable_log:
    LOGGING_CONFIG = None
    LOGGING = {}
else:
    # Try loading logging configuration from your project
    try:
        from Garmen_textile.logging import LOGGING
    except ImportError:
        LOGGING = {}

# -------------------------------------------------------------
# Session Configuration
# -------------------------------------------------------------
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Store sessions in the database