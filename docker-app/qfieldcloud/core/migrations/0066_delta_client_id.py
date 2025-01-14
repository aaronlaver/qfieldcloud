# Generated by Django 3.2.18 on 2023-05-09 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0065_auto_20230422_1101"),
    ]

    operations = [
        migrations.AddField(
            model_name="delta",
            name="client_id",
            field=models.UUIDField(db_index=True, null=True, editable=False),
        ),
        migrations.RunSQL(
            "UPDATE core_delta SET client_id = COALESCE((content->>'clientId')::uuid, deltafile_id)",
            migrations.RunSQL.noop,
        ),
        migrations.AlterField(
            model_name="delta",
            name="client_id",
            field=models.UUIDField(db_index=True, null=False, editable=False),
        ),
    ]
