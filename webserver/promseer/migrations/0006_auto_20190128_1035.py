# Generated by Django 2.1.5 on 2019-01-28 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promseer', '0005_auto_20190128_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predicttarget',
            name='metric_encode',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='metric encode'),
        ),
    ]
