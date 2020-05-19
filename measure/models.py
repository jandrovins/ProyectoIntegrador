from django.db import models
from django.core.validators import MinValueValidator
from decimal import *
import uuid

TERRENOS_VALIDOS = [
        ('Planicie', 'Planicie'),
        ('Ladera', 'Ladera'),
        ('Cenagoso', 'Cenagoso'),
        ('Desertico', 'Desertico'),
        ]

class Measure(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    codigo = models.CharField(max_length=30, null=True, blank=True)
    latitud = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    longitud = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    terreno = models.CharField(max_length=30, choices=TERRENOS_VALIDOS, blank=True, null=True)
    area = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))], blank=True, null=True)
