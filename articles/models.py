from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=40, verbose_name='Тег')
    url = models.CharField(max_length=40, default=12345)
    articles = models.ManyToManyField(Article, related_name='tags', through='Scope')

    def __str__(self):
        return self.name

class Scope(models.Model):
    tag = models.ForeignKey (Tag, on_delete=models.CASCADE, related_name='scopes' )
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    main = models.BooleanField(verbose_name='Основной')
    class Meta:
        ordering = ['-main']
