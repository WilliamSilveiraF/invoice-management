# Generated by Django 4.0.6 on 2022-07-24 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('ein', models.TextField()),
                ('structure', models.CharField(choices=[('LLC', 'LIMITED LIABILITY COMPANY'), ('SP', 'SOLE PROPRIETORSHIPS'), ('PARTNER', 'PARTNERSHIP'), ('CORP', 'CORPORATION'), ('S CORP', 'S CORPORATION'), ('ND', 'NOT DEFINED')], default='ND', max_length=7)),
                ('address', models.JSONField(default=dict)),
                ('cellphone', models.TextField()),
                ('creationDate', models.DateTimeField()),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.JSONField(default=dict)),
                ('productAmount', models.IntegerField()),
                ('total', models.FloatField()),
                ('issueDate', models.TextField()),
                ('base64', models.TextField(null=True)),
                ('costumer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
        ),
    ]
