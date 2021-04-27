from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=60)
    picture_url = models.CharField(max_length=60)

    class Location(models.TextChoices):
        HOFUDBORGARSVAEDI = 'HO', _('Höfuðborgarsvæðið')
        VESTFIRDIR = 'VF', _('Vestfirðir')
        VESTURLAND = 'VL', _('Vesturland')
        SUDURLAND = 'SL', _('Suðurland')
        AUSTURLAND = 'AL', _('Austurland')

    location = models.CharField(
        max_length=2,
        choices=Location.choices,
        default=Location.HOFUDBORGARSVAEDI,
    )

class Job(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=60)

class Tags(models.Model):
    name = models.CharField(max_length=20)

class ProfileTags(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)

class JobTags(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)

