# Generated by Django 4.1.4 on 2023-02-04 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A_brief_Discription', models.TextField(default='Tell Your Condition ...', max_length=1000)),
                ('clip', models.FileField(default='', upload_to='videos/%Y/%m/%d/')),
            ],
        ),
    ]
