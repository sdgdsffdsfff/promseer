# Generated by Django 2.1.5 on 2019-02-14 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promseer', '0012_auto_20190212_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registermetric',
            name='train_status',
            field=models.IntegerField(default=0),
        ),
    ]
