# Generated by Django 4.1 on 2022-12-12 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0043_sub_data_prx1_eighth_period_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_data_prx1',
            name='EIGHTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx1',
            name='FIFTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx1',
            name='FIRST_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx1',
            name='FOURTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx1',
            name='NINETH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx1',
            name='SECOND_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx1',
            name='SEVENTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx1',
            name='SIXTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx1',
            name='THIRD_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]