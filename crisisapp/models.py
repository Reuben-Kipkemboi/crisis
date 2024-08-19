from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_respondent = models.BooleanField('Is respondent', default=False)
    is_public = models.BooleanField('Is public', default=False)
    
    
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    username=models.CharField(max_length=100,blank=True,null=True)
    user_email=models.EmailField(max_length=100,blank=True,null=True)
    profile_pic=CloudinaryField('image')
    biography=models.TextField(blank=True,null=True)
    contact_number=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def profile_update(self,id,profile):
        updated_profile=Profile.objects.filter(id=id).update(profile)
        return updated_profile

    def __str__(self):
        return str(self.username)