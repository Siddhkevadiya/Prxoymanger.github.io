# Generated by Django 4.1 on 2023-05-20 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0050_remove_sub_timetable1_eighth_period_1_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='sub_Data_PRXs',
        ),
        migrations.RemoveField(
            model_name='sub_timetable10',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable11',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable12',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable13',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable14',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable15',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable16',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable17',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable18',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable19',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable2',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable20',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable21',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable22',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable23',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable24',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable25',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable26',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable27',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable28',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable29',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable3',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable30',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable31',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable32',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable33',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable34',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable35',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable36',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable37',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable38',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable39',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable4',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable40',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable41',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable42',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable43',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable44',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable45',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable46',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable47',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable48',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable49',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable5',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable50',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable6',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable7',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable8',
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='sub_timetable9',
            name='Teacher',
        ),
        migrations.AddField(
            model_name='timetable',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='data_prx',
            name='Table_Id',
            field=models.CharField(default=3, max_length=2, unique=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='Table_Id',
            field=models.CharField(default=47, max_length=2, unique=True),
        ),
        migrations.DeleteModel(
            name='sub_TimeTable1',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable10',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable11',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable12',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable13',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable14',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable15',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable16',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable17',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable18',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable19',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable2',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable20',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable21',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable22',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable23',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable24',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable25',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable26',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable27',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable28',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable29',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable3',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable30',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable31',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable32',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable33',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable34',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable35',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable36',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable37',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable38',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable39',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable4',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable40',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable41',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable42',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable43',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable44',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable45',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable46',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable47',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable48',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable49',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable5',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable50',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable6',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable7',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable8',
        ),
        migrations.DeleteModel(
            name='sub_TimeTable9',
        ),
    ]
