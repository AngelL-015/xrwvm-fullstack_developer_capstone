from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Car Make model
class CarMake(models.Model):
    # Fields
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    # Return the name as a string representation
    def __str__(self):
        return self.name


# Car Model model
class CarModel(models.Model):
    # Many-to-Many Relationship
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    # Fields
    dealer_id = models.IntegerField()
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('COUPE', 'Coupe'),
        ('HATCHBACK', 'Hatchback'),
        ('CONVERTIBLE', 'Convertible'),
        ('WAGON', 'Wagon'),
        ('SUV', 'SUV'),
        ('CROSSOVER', 'Crossover'),
        ('PICKUP', 'Pickup Truck'),
        ('MINIVAN', 'Minivan'),
        ('VAN', 'Van')
    ]
    type = models.CharField(max_length=11, choices=CAR_TYPES, default='Sedan')
    year = models.IntegerField(default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ]
    )

    # Return the name as a string representation
    def __str__(self):
        return self.name
