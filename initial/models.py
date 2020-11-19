from django.db import models


class ToDo(models.Model):
    text = models.CharField(max_length=200)
    added_date = models.DateTimeField(auto_now=True)

