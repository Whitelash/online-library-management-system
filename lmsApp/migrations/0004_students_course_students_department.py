from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsApp', '0003_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='course',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='department',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
