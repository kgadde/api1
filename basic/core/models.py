from django.db import models

class SavedEmbeds(models.Model):
    type = models.CharField(max_length=15, null=True)
    provider_url = models.URLField(null=True)
    provider_name = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    html = models.TextField(null=True)
    width = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    thumbnail_url = models.URLField(null=True)
    thumbnail_width = models.IntegerField(null=True)
    thumbnail_height = models.IntegerField(null=True)
    author_url = models.URLField(null=True)
    author_name = models.CharField(max_length=100, null=True)
    version = models.DecimalField(max_digits=4, decimal_places=2, null=True)
