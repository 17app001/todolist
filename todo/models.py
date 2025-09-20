from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    date_completed = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.title} 建立時間:{self.created.strftime("%Y-%m-%d %H:%M:%S")} 是否重要:{self.important}"
