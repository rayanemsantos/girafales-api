from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone

from base_auth.models import AuthUser
from general.models import Address

class Teacher(AuthUser):

    registration_id = models.PositiveIntegerField(_("matrícula"), null=True, blank=True) 
    formacao = models.CharField(_("formação"), max_length=255, null=True, blank=True) 
    address = models.ForeignKey(Address, verbose_name=_("endereço"),
                                on_delete=models.CASCADE, null=True, blank=True)
    creation_datetime = models.DateTimeField(editable=False)
    edition_datetime = models.DateTimeField(_("última atualização"), null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.creation_datetime:
            self.creation_datetime = timezone.now()
        self.edition_datetime = timezone.now()
        return super(Teacher, self).save(*args, **kwargs)