# Generated by Django 4.2.4 on 2023-08-07 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("boards", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="board", name="image",),
        migrations.RemoveField(model_name="board", name="view_count",),
        migrations.RemoveField(model_name="board", name="writer",),
        migrations.DeleteModel(name="Comment",),
    ]