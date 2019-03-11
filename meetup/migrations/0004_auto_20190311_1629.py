# Generated by Django 2.1.7 on 2019-03-11 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0003_auto_20190311_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
