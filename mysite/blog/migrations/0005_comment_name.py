# Generated by Django 4.2 on 2025-03-31 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment_comment_blog_commen_created_0e6ed4_idx'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='default name', max_length=80),
            preserve_default=False,
        ),
    ]
