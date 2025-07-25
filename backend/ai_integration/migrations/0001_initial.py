# Generated by Django 5.2.4 on 2025-07-12 09:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelAccessHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=255)),
                ('access_time', models.DateTimeField(auto_now_add=True)),
                ('accessed_by', models.CharField(max_length=255)),
                ('attempts_count', models.PositiveIntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='ChatHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_question', models.TextField()),
                ('model_response', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_parent', models.BooleanField(default=False)),
                ('parent_chat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='child_chats', to='ai_integration.chathistory')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
