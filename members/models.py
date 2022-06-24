from django.db import models

# Create your models here.
class Members(models.Model):
  supplier_or_receiver=models.CharField(max_length=8)
  email_id = models.CharField(max_length=255)
  # Create your models here.`
