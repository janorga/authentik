# Generated by Django 5.0.7 on 2024-07-23 12:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_core", "0038_source_groups_list_property_mappings_and_more"),
        ("authentik_sources_plex", "0003_alter_plexsource_plex_token"),
    ]

    operations = [
        migrations.CreateModel(
            name="PlexSourcePropertyMapping",
            fields=[
                (
                    "propertymapping_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="authentik_core.propertymapping",
                    ),
                ),
            ],
            options={
                "verbose_name": "Plex Source Property Mapping",
                "verbose_name_plural": "Plex Source Property Mappings",
            },
            bases=("authentik_core.propertymapping",),
        ),
    ]
