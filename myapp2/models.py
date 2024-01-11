from django.db import models

class music(models.Model):
      name=models.CharField(max_length=20)
      song=models.FileField(upload_to='media')
