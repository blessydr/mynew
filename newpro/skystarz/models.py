from django.db import models
class moon(models.Model):
    title=models.CharField(max_length=100)
# Create your models here.
class star(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=10)
    mesg=models.CharField(max_length=300)
    new_title=models.ForeignKey(moon,null=True,on_delete=models.CASCADE)