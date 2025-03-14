# Generated by Django 2.2.10 on 2020-06-14 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_exam', '0002_category_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('news', models.TextField()),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'managed': True, 'verbose_name': 'video', 'verbose_name_plural': 'videos'},
        ),
    ]
