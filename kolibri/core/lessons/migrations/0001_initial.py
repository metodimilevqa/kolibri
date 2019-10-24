# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-18 01:21
from __future__ import unicode_literals

import django.db.models.deletion
import jsonfield.fields
import morango.models
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("kolibriauth", "0007_auto_20171226_1125")]

    operations = [
        migrations.CreateModel(
            name="Lesson",
            fields=[
                (
                    "id",
                    morango.models.UUIDField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "_morango_dirty_bit",
                    models.BooleanField(default=True, editable=False),
                ),
                ("_morango_source_id", models.CharField(editable=False, max_length=96)),
                (
                    "_morango_partition",
                    models.CharField(editable=False, max_length=128),
                ),
                ("name", models.CharField(max_length=50)),
                (
                    "description",
                    models.CharField(blank=True, default="", max_length=200),
                ),
                ("resources", jsonfield.fields.JSONField(blank=True, default=[])),
                ("is_active", models.BooleanField(default=False)),
                ("is_archived", models.BooleanField(default=False)),
                (
                    "collection",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lessons",
                        to="kolibriauth.Collection",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lessons_created",
                        to="kolibriauth.FacilityUser",
                    ),
                ),
                (
                    "dataset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="kolibriauth.FacilityDataset",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="LessonAssignment",
            fields=[
                (
                    "id",
                    morango.models.UUIDField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "_morango_dirty_bit",
                    models.BooleanField(default=True, editable=False),
                ),
                ("_morango_source_id", models.CharField(editable=False, max_length=96)),
                (
                    "_morango_partition",
                    models.CharField(editable=False, max_length=128),
                ),
                (
                    "assigned_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="assigned_lessons",
                        to="kolibriauth.FacilityUser",
                    ),
                ),
                (
                    "collection",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="assigned_lessons",
                        to="kolibriauth.Collection",
                    ),
                ),
                (
                    "dataset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="kolibriauth.FacilityDataset",
                    ),
                ),
                (
                    "lesson",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="assigned_groups",
                        to="lessons.Lesson",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
    ]
