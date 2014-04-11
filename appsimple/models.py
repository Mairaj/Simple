from django.db import models
from django.forms import ModelForm

class Name(models.Model):
     """ """
     name = models.CharField(max_length=10)
     age = models.IntegerField()

     def __unicode__(self):
         """ """
         return self.name

     class Meta:
         """ """
         verbose_name = 'Name'
         verbose_name_plural = 'Names'


class NameForm(ModelForm):
    """ """
    class Meta:
       """ """
       model = Name
       

