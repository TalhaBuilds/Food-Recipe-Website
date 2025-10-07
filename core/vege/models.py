from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)

    def __str__(self):
        return self.name
