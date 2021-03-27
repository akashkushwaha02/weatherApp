from django.db import models

# Create your models here.
class City(models.Model):
    city = models.CharField(null=False,max_length=40)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city