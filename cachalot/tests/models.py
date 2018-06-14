# coding: utf-8

from __future__ import unicode_literals

from django.conf import settings
from django.contrib.postgres.fields import (
    ArrayField, HStoreField,
    IntegerRangeField, JSONField, FloatRangeField, DateRangeField,
    DateTimeRangeField)
from django.db.models import (
    Model, CharField, ForeignKey, BooleanField, DateField, DateTimeField,
    ManyToManyField, BinaryField, IntegerField, GenericIPAddressField,
    FloatField, DecimalField, DurationField, UUIDField, SET_NULL, PROTECT)


class Test(Model):
    name = CharField(max_length=20)
    owner = ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True,
                       on_delete=SET_NULL)
    public = BooleanField(default=False)
    date = DateField(null=True, blank=True)
    datetime = DateTimeField(null=True, blank=True)
    permission = ForeignKey('auth.Permission', null=True, blank=True,
                            on_delete=PROTECT)

    # We can’t use the exact names `float` or `decimal` as database column name
    # since it fails on MySQL.
    a_float = FloatField(null=True, blank=True)
    a_decimal = DecimalField(null=True, blank=True,
                             max_digits=5, decimal_places=2)
    bin = BinaryField(null=True, blank=True)
    ip = GenericIPAddressField(null=True, blank=True)
    duration = DurationField(null=True, blank=True)
    uuid = UUIDField(null=True, blank=True)

    class Meta:
        ordering = ('name',)


class TestParent(Model):
    name = CharField(max_length=20)


class TestChild(TestParent):
    public = BooleanField(default=False)
    permissions = ManyToManyField('auth.Permission', blank=True)


class PostgresModel(Model):
    int_array = ArrayField(IntegerField(null=True, blank=True), size=3,
                           null=True, blank=True)

    hstore = HStoreField(null=True, blank=True)

    json = JSONField(null=True, blank=True)

    int_range = IntegerRangeField(null=True, blank=True)
    float_range = FloatRangeField(null=True, blank=True)
    date_range = DateRangeField(null=True, blank=True)
    datetime_range = DateTimeRangeField(null=True, blank=True)

    class Meta:
        # Tests schema name in table name.
        db_table = '"public"."cachalot_postgresmodel"'
