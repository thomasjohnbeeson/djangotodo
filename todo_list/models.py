from django.db import models

# Create your models here.

class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self): #this subfunction defines what appears as th object, in this case juste the item name
        return str(self.item) + ' ' + str(self.completed)