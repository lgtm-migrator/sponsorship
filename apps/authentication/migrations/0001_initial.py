# Generated by Django 3.0.7 on 2020-06-14 09:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_id', models.UUIDField(default=uuid.UUID('e6dc577d-49d3-4683-aa13-536119d85e71'), unique=True)),
                ('username', models.CharField(db_index=True, max_length=255, unique=True)),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('password', models.CharField(max_length=512)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_sponsor', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('role', models.CharField(choices=[('STD', 'Student'), ('STF', 'Staff'), ('SPN', 'Sponsor')], default='STD', max_length=3)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('student_id', models.UUIDField(default=uuid.UUID('ea31749d-b668-4225-aa5c-c6ae5a5fc93a'), unique=True)),
                ('phone', models.CharField(max_length=16)),
                ('national_id', models.FileField(max_length=255, null=True, upload_to='')),
                ('birth_certificate', models.FileField(max_length=255, null=True, upload_to='')),
                ('attached_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('course', models.ForeignKey(db_column='course_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='schools.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('sponsor_id', models.UUIDField(default=uuid.UUID('d4213310-e1f9-421c-b678-bf5770eb5fac'), unique=True)),
                ('phone_number', models.CharField(max_length=16)),
                ('attached_account', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]