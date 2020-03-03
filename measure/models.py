from django.db import models
import uuid

class Measure(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(verbose_name='type', max_length=20, default="distance")
    value = models.IntegerField(verbose_name='valor', default="0")
    scale = models.CharField(max_length=1, default="m")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
