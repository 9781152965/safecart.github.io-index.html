# Generated by Django 3.1.2 on 2020-11-01 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0005_productimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='newproducts')),
                ('marked_price', models.PositiveIntegerField()),
                ('selling_price', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('warranty', models.CharField(blank=True, max_length=300, null=True)),
                ('return_policy', models.CharField(blank=True, max_length=300, null=True)),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.category')),
            ],
        ),
    ]
