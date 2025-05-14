from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)  #字串中blank=True是可以為空字串
    created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True)  #null=True為空物件
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null = True)
    
    def __str__(self):
        return f'{self.id} - {self.title} - {self.created}'





