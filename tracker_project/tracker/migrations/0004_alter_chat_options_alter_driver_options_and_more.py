# Generated by Django 4.1.4 on 2022-12-21 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_alter_tracker_options_chat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chat',
            options={'ordering': ['-date_added', 'date_edited']},
        ),
        migrations.AlterModelOptions(
            name='driver',
            options={'ordering': ['-email']},
        ),
        migrations.AlterModelOptions(
            name='tracker',
            options={'ordering': ['-date_added', 'date_edited']},
        ),
    ]