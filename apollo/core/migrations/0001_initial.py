# Generated by Django 2.0 on 2017-12-16 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=50)),
                ('location_string', models.CharField(max_length=50)),
                ('lat_long', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RoomData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('temp', models.FloatField()),
                ('noise', models.FloatField()),
                ('occupied', models.BooleanField()),
                ('headcount', models.SmallIntegerField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Room')),
            ],
        ),
    ]
