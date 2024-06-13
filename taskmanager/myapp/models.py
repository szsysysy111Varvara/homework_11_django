from django.db import models

class Task(models.Model):
    objects = None
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    deadline = models.DateTimeField()

    def __str__(self):
        return self.title
