from django.db import models

# Create your models here.
class Food(models.Model):
    title = models.CharField(max_length=200)
    prot = models.IntegerField(default=0)
    fats = models.IntegerField(default=0)
    carb = models.IntegerField(default=0)
    calories = models.IntegerField(default=0)
    def __str__(self):
        return self.title
