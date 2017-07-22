from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Project(models.Model):
    FILE_TYPES = (('J', 'json'), ('C', 'config'))
    project_name = models.CharField(max_length=50, unique=True)
    file_type = models.CharField(max_length=1, choices=FILE_TYPES)

    def __str__(self):
        return self.project_name

@python_2_unicode_compatible
class Content(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    config_text = models.TextField(blank=True)

    def __str__(self):
        return self.config_text
