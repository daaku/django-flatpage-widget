django-flatpage-widget
======================

Patches the flatpage Admin to use a custom Widget for the content. This can be
used with widgets from [django-rte-widgets][1].

Install the app and provide a setting like such:

    FLATPAGE_WIDGET = ('rte_widgets.yui.YuiTextarea', {'config': {'height': '400px', 'width': '700px', 'format': 'xhtml'}})

The setting must be a tuple of two elements, where the first is a resolved to a
callable using django's `get_callable` and the second is a dict which will be
passed to the callable as keyword arguments. This works with standard Widget
classes.
