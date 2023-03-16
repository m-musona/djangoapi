# Generated by Django 4.1.7 on 2023-03-05 18:28

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('api', '0003_tag_stories_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='stories',
            name='tag',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]