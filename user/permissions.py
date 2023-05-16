from django.contrib.auth.models import Permission
from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        permission_codename = 'view_user'  # Specify the permission codename
        if Permission.objects.filter(group__user=request.user, codename=permission_codename):
            return True
        return False
