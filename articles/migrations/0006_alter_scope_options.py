# Generated by Django 4.0.5 on 2022-06-15 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_tag_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'ordering': ['main']},
        ),
    ]