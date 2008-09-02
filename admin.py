from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOrig

class FlatPageAdmin(FlatPageAdminOrig):
    change_form_template = 'flatpages_yui_rte/change_form.html'

    class Media:
        js = (
                'http://yui.yahooapis.com/combo?2.5.2/build/yahoo-dom-event/yahoo-dom-event.js&2.5.2/build/container/container_core-min.js&2.5.2/build/menu/menu-min.js&2.5.2/build/element/element-beta-min.js&2.5.2/build/button/button-min.js&2.5.2/build/editor/editor-beta-min.js',
        )
        css = {
            'all': ('http://yui.yahooapis.com/2.5.2/build/assets/skins/sam/skin.css',)
        }

# We have to unregister it, and then reregister
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
