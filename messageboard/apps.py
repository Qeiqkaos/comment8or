from django.apps import AppConfig
from django.contrib.admin import apps


class MessageboardConfig(AppConfig):
    name = 'messageboard'


class C8AdminConfig(apps.AdminConfig):
    default_site = 'admin.C8AdminSite'
