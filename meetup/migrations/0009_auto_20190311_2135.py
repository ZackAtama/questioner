# Generated by Django 2.1.7 on 2019-03-11 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0008_auto_20190311_1948'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meetingtag',
            old_name='meeting',
            new_name='meetup',
        ),
    ]
