from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=50)
    posted_date = models.DateField()
    details_url = models.URLField()

    def __str__(self):
        return self.title
