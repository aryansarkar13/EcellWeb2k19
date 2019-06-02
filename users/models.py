from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    USER_TYPE = (
        ('GST', 'Guest'),
        ('VLT', 'Voluteer'),
        ('EXE', 'Executive'),
        ('MNG', 'Manager'),
        ('HCO', 'Head Co-ordinator'),
        ('OCO', 'Overall Co-ordinator'),
        ('CAB', 'Campus Ambassador'),
    )

    username    = models.CharField(max_length=32, unique=True)
    email       = models.CharField(max_length=64, unique=True)
    otp         = models.CharField(max_length=4, blank=True, null=True)
    verified    = models.BooleanField(default=False)
    contact     = models.CharField(max_length=10)
    bquiz_score = models.IntegerField(default=0)
    avatar      = models.ImageField(upload_to='static/uploads/avatar',
                                    null=True, blank=True)
    user_type   = models.CharField(max_length = 3,choices=USER_TYPE,
                                    default='GST')
    linkedin    = models.URLField(max_length=64, null=True, blank=True)
    facebook    = models.URLField(max_length=64, null=True, blank=True)
    
    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "ECellUser"
        verbose_name_plural = "ECellUsers"

class CampusAmbassadurProfile(models.Model):

    user        = models.OneToOneField(CustomUser, on_delete=models.CASCADE,
                                related_name='CampuCampusAmbassadurProfile')
    college     = models.CharField(max_length=128, null=False, blank=False)

    # Scores for Campus Ambassadors
    total_score = models.IntegerField(default=0)        #Total Score
    fb_score    = models.IntegerField(default=0)        #Facebook Score
    tw_score    = models.IntegerField(default=0)        #Twitter Score
    li_score    = models.IntegerField(default=0)        #LinkedIn Score
    wp_score    = models.IntegerField(default=0)        #Whatsapp Score
