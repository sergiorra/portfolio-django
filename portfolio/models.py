from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)  # blank=True -> field not mandatory

    def __str__(self):
        # for better visualization in admin page
        return self.title
