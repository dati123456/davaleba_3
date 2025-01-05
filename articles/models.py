from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    views = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title



