# Generated by Django 3.0.8 on 2020-08-26 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat_posts', '0014_use_django_names'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='chat_posts.Rooms'),
        ),
    ]