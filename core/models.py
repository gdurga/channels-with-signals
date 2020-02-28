from django.conf import settings
from django.db import models


class Item(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)

