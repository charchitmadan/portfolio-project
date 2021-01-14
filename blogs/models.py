from django.db import models

# Create your models here.
class Blog(models.Model) :
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField()
    body = models.TextField()         #Used TextField instead of CharField because TextField allows to enter more text. We can use CharField also.
    image = models.ImageField(upload_to = "images/")

    def summary(self) :
        return self.body[:100]

    def pretty_time(self) :
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self) :
        return self.title
