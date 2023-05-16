from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
from django.contrib.auth.models import Group


class User(AbstractUser):
    profiles = models.ManyToManyField(
        "user.Profile", verbose_name="Níveis")


class Profile(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nome Perfil")
    permissions = models.ManyToManyField(Permission, through="user.ProfilePermission")

    def __str__(self):
        return self.name


class ProfilePermission(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            "profile",
            "permission",
        )

