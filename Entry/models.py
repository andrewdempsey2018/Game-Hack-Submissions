from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=30)
    upload = models.FileField(upload_to="uploads/")

    def __str__(self):
        return self.title

