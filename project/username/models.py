from django.db import models

class UserInfo(models.Model):
    uname=models.CharField(max_length=10)
    upwd=models.CharField(max_length=20)

    def __str__(self):
        return '%d',self.pk
    
