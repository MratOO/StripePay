from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=64, blank=True)
    description = models.TextField(blank=True)
    price = models.IntegerField(blank=True)

 
    def __str__(self):
        return self.name
