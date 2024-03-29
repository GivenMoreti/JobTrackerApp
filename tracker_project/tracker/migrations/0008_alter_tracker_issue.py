# Generated by Django 4.2 on 2023-07-02 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tracker", "0007_alter_tracker_issue"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tracker",
            name="issue",
            field=models.ForeignKey(
                max_length=300,
                on_delete=django.db.models.deletion.CASCADE,
                to="tracker.category",
            ),
        ),
    ]
