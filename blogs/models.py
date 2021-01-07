from django.db import models

# Create your models here.
class Blog(models.Model) :
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField()
    body = models.TextField()         #Used TextField instead of CharField because TextField allows to enter more text. We can use CharField also.
    image = models.ImageField(upload_to = "images/")
