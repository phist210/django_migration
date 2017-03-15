from django.db import models


class Bills(models.Model):
    bill = models.CharField(max_length=20)
    amount = models.IntegerField()
    due_date = models.DateTimeField(null=True, blank=True)
