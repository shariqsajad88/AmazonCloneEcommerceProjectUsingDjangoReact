# Generated by Django 5.0.6 on 2024-08-27 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OrderService', '0005_remove_purchaseorder_due_amount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseorder',
            name='total_amount',
        ),
    ]