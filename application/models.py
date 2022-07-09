import jsonfield
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Platform(models.Model):
    platform_name = models.CharField(max_length=100)
    conf = jsonfield.JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kinds', verbose_name=_('kind'),)

    def __str__(self):
        return self.platform_name

    class Meta:
        ordering = ['platform_name']
