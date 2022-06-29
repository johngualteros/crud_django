from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255,verbose_name='Title')
    image = models.ImageField(upload_to='images/',verbose_name='Image')
    description = models.TextField(null=True,verbose_name='Description')

    def __str__(self):
        row='Title'+self.title+'-'+'Description'+self.description
        return self.title
