from django.db import models


class Bills(models.Model):
    bill = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    due_date = models.DateTimeField(null=True, blank=True)
