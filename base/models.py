
from djongo import models

# Create your models here.

class Charquestions(models.Model):
    question = models.TextField()

    def __str__(self):
        return self.question
    
class Chardata(models.Model):
    name = models.TextField()
    male = models.BooleanField()
    female = models.BooleanField()
    human = models.BooleanField()
    youtuber= models.BooleanField()
    actor= models.BooleanField()
    real= models.BooleanField()
    Indian= models.BooleanField()
    American= models.BooleanField()
    scientist= models.BooleanField()
    Singer = models.BooleanField()
    Politician = models.BooleanField(default=False)
    def __str__(self):
        return self.name
