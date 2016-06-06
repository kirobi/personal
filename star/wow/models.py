from django.db import models
#from django.contrib.auth.models import User
class book(models.Model):
    name= models.CharField(max_length=50)
    author= models.CharField(max_length=50)
    publisher=models.CharField(max_length=50)
    #user=models.ForeignKey(User)
    def __unicode__(self):
        return self.name
