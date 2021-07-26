# Generated by Django 3.2.5 on 2021-07-26 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='ComunicacaoAgendada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('mensagem', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ComunicacaoAgendada_Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('via', models.IntegerField(choices=[(0, 'Email'), (1, 'Sms'), (2, 'Push'), (3, 'Whatsapp')])),
                ('status', models.IntegerField(choices=[(0, 'Agendada'), (1, 'Enviada'), (2, 'Cancelada')], default=0)),
                ('comunicacao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.comunicacaoagendada')),
                ('destinatario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.cliente')),
            ],
        ),
    ]