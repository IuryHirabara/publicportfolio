from django.db import models

# Create your models here.


class Card(models.Model):
    title = models.CharField(max_length=10)
    border = models.CharField(max_length=20)
    text = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.title


class Technology(models.Model):
    title = models.CharField(max_length=30, unique=True)

    def __str__(self) -> str:
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    order = models.PositiveSmallIntegerField(unique=True)
    url = models.URLField(max_length=100)
    card = models.ForeignKey(Card, on_delete=models.PROTECT)
    technologies = models.ManyToManyField(Technology)
    online = models.BooleanField()

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ("order",)
