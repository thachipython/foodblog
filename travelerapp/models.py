from django.db import models

# Create your models here.

class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='picture')
    des=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)