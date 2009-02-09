from django.conf import settings
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.core.urlresolvers import get_callable


class FlatPageAdminWidget(FlatPageAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            c, k = getattr(settings, 'FLATPAGE_WIDGET')
            kwargs['widget'] = get_callable(c)(**k)
        return super(FlatPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)

# We have to unregister it, and then reregister
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdminWidget)
