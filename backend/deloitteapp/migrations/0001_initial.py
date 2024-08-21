# Generated by Django 4.2.5 on 2023-10-02 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(default='', max_length=255)),
                ('student_email', models.EmailField(max_length=254, unique=True)),
                ('student_password', models.CharField(default='', max_length=255)),
                ('student_birth_date', models.DateField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(default='', max_length=255)),
                ('teacher_email', models.EmailField(default='', max_length=254, unique=True)),
                ('teacher_password', models.CharField(default='', max_length=255)),
                ('teacher_birth_date', models.DateField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=255)),
                ('subject_workload', models.IntegerField()),
                ('teacher_name', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='deloitteapp.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.DecimalField(decimal_places=2, max_digits=5)),
                ('student_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deloitteapp.student')),
                ('subject_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deloitteapp.subject')),
            ],
        ),
    ]
