from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.db import models

class AppUser(User):
    username_validator = ASCIIUsernameValidator()

    class Meta:
        proxy = True  # If no new field is added.

class UrlTab(models.Model):
    appuser = models.ForeignKey(AppUser)
    url = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    public_url = models.BooleanField(default=False)

    def __str__(self):
        return self.url


class TagTab(models.Model):
    tagid = models.ManyToManyField(UrlTab)
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag

    def save(self, *args, **kwargs):
        self.username = self.username.lower()
        super().save(*args, **kwargs)