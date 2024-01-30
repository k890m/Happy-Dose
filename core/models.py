from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True, max_length = 300)
    profile_img = models.ImageField(upload_to='profile_images', default='autoprofile.png') 
    location = models.CharField(blank=True ,max_length=150)
    
    def __str__(self):
        return self.user.get_username() 
    
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    num_likes = models.IntegerField(default=0)
    
    def __str__(self) :
        return self.user