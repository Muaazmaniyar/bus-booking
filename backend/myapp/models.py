from django.db import models

# Create your models here.
class Bus(models.Model):
    name = models.CharField(max_length=100)
    route = models.CharField(max_length=200)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    seats_available = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.route})"