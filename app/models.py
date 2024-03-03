from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Room(models.Model):
    room_no=models.IntegerField()
    vacant=models.IntegerField(default=5)
    def __str__(self):
        return str(self.room_no)
class Book(models.Model):
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    student=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(s):
        return s.student
class Complaint(models.Model):
    student=models.ForeignKey(User,on_delete=models.CASCADE)
    complaint=models.CharField(max_length=100)
    def __str__(s):
        return s.student