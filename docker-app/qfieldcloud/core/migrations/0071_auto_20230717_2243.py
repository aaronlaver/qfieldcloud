# Generated by Django 3.2.18 on 2023-07-17 20:43

import migrate_sql.operations
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0070_alter_project_is_public"),
    ]

    operations = [
        migrate_sql.operations.DeleteSQL(
            name="core_delta_geom_insert_trigger",
            sql="\n            DROP TRIGGER IF EXISTS core_delta_geom_insert_trigger ON core_delta\n        ",
            reverse_sql="\n            CREATE TRIGGER core_delta_geom_insert_trigger BEFORE INSERT ON core_delta\n            FOR EACH ROW\n            EXECUTE FUNCTION core_delta_geom_trigger_func()\n        ",
        ),
        migrate_sql.operations.CreateSQL(
            name="core_delta_geom_insert_trigger",
            sql="\n            CREATE TRIGGER core_delta_geom_insert_trigger BEFORE INSERT ON core_delta\n            FOR EACH ROW\n            EXECUTE FUNCTION core_delta_geom_trigger_func()\n        ",
            reverse_sql="\n            DROP TRIGGER IF EXISTS core_delta_geom_insert_trigger ON core_delta\n        ",
        ),
    ]
