# Generated by Django 4.2.1 on 2023-05-22 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_alter_listing_category_alter_listing_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Bikes', 'Bikes'), ('Books&Sports', 'Books&Sports'), ('Cars', 'Cars'), ('Mobiles', 'Mobiles'), ('Furniture', 'Furniture'), ('Jobs', 'Jobs'), ('Electronics', 'Electronics'), ('Property', 'Property'), ('Fashion', 'Fashion')], max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.CharField(choices=[('GJ', 'Gujarat'), ('TN', 'Tamil Nadu'), ('NL', 'Nagaland'), ('MZ', 'Mizoram'), ('JH', 'Jharkhand'), ('AR', 'Arunachal Pradesh'), ('OD', 'Odisha'), ('AS', 'Assam'), ('PB', 'Punjab'), ('WB', 'West Bengal'), ('CG', 'Chhattisgarh'), ('MI', 'Sikkim'), ('MN', 'Manipur'), ('GA', 'Goa'), ('ML', 'Meghalaya'), ('TR', 'Tripura'), ('UK', 'Uttarakhand'), ('TS', 'Telegana'), ('KL', 'Kerala'), ('UP', 'Uttar Pradesh'), ('KA', 'Karnataka'), ('BR', 'Bihar'), ('MH', 'Maharashtra'), ('HP', 'Haryana'), ('MP', 'Madhya Pradesh'), ('AP', 'Andhra Pradesh'), ('RJ', 'Rajasthan')], max_length=100),
        ),
    ]