# Generated by Django 4.2.7 on 2023-11-17 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msistore', '0009_remove_order_total_alter_order_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='msistore.OrderItem', to='msistore.product'),
        ),
    ]