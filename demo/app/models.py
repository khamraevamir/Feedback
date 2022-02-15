from django.db import models


class Feedback(models.Model):
    name = models.CharField('Имя Фамилия', max_length=40)
    number = models.CharField('Номер телефона',max_length=15)
    city = models.CharField('Город телефона',max_length=20)
    status = models.BooleanField('Статус', default=False, null=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return 'Город: ' + self.city + ' Имя: ' + self.name + ' ' + str(self.number)