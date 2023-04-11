from django.contrib import admin


class C8AdminSite(admin.AdminSite):
    site_title = 'c8 site admin'
    site_header = 'c8admin administration'
    index_title = 'c8admin site admin'
    logout_template = 'comment8or/logged_out.html'
