from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ChaiVarity(models.Model):
  CHAI_TYPE_CHOICES = [
    ('ML', 'MASALA'),
    ('GR', 'GREEN'),
    ('KL', 'KIWI'),
    ('PL', 'PLAIN'),
    ('EL', 'ELAICHI')
  ]

  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to='chais/')
  date_added = models.DateTimeField(default=timezone.now)
  type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES)
  description = models.TextField(default='')
  price = models.DecimalField(max_digits=10, decimal_places=2, default=10)

  def __str__(self):
    return self.name
# Create your models here.
