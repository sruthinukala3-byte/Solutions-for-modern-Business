from django.db import models


class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    service = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class BusinessAnalysis(models.Model):
    business_name = models.CharField(max_length=150)
    question = models.TextField()
    monthly_revenue = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )
    monthly_expenses = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business_name
