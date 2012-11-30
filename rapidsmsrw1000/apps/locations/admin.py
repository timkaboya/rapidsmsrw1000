#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.contrib import admin
from rapidsms.contrib.locations.models import LocationType
from .models import Location

admin.site.register(Location)
admin.site.register(LocationType)
