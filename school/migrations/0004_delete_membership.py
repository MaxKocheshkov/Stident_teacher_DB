# Generated by Django 2.2.10 on 2020-08-15 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_membership'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Membership',
        ),
    ]