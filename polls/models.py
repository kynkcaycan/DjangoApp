from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    #question_text sütun adı
    #max_length sütun uzunluğu
    #models.CharField() veri tipi
    #models.IntegerField() veri tipi
    #models.DateTimeField() veri tipi
    #models.ForeignKey() veri tipi
    #models.CASCADE() veri tipi
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
