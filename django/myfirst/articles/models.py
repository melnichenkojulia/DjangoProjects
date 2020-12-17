from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Article(models.Model):
    article_title = models.CharField('Article Cat', max_length=20)
    article_text = models.TextField('cat is an animal')
    pub_date = models.DateTimeField('date of publishing')

    def __str__(self):
        return self.article_title

    def date_recently(self):
        return self.pub_date>=(timezone.now()-datetime.timedelta(days=3))


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('Author`s name', max_length=50)
    comment_text = models.CharField('cat is an animal', max_length=500)

    def __str__(self):
        return self.author_name


