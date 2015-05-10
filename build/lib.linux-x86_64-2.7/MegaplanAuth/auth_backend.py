# -*- coding: utf-8 -*-


from django.contrib.auth.backends import ModelBackend
from django.conf import settings

from django.contrib.auth import get_user_model
from .megaplan.megaplan import Client

User = get_user_model()

class MegaplanAuthBackends(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        host = getattr(settings, 'MEGAPLAN_AUTH_HOST', None)
        greate_new_user = getattr(settings, 'MEGAPLAN_AUTH_GREATE_USER', True)
        user_active = getattr(settings, 'MEGAPLAN_AUTH_USER_ACTIVE', True)
        super_user_ids = getattr(settings, 'MEGAPLAN_AUTH_SUPER_USER_IDS', [])
        staf_user_ids = getattr(settings, 'MEGAPLAN_AUTH_STAF_USER_IDS', [])
        if host is None:
            return None
        try:
            c = Client(host)
            access_id, secret_key, EmployeeId = c.authenticate(login=username, password=password)
            c = Client(host, access_id, secret_key)
            employee = c.get_employee_card(EmployeeId)
            employee = employee.get('employee')
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                if greate_new_user is True:
                    created = True
                    user = User(username=username)
                    user.set_password(password)
                    user.is_active = True
                else:
                    user = None
            if user is not None:
                if employee is not None:
                    user.first_name = employee.get('FirstName')
                    user.last_name = employee.get('LastName')
                    user.email = employee.get('Email')
                EmployeeId = int(EmployeeId)
                if EmployeeId in super_user_ids:
                    user.is_superuser = True
                if EmployeeId in staf_user_ids:
                    user.is_staff = True
                if created is True and user_active is True:
                    user.is_active = True
                else:
                    user.is_active = False
                user.save()
                # @stilstodo: посмотреть возможно надо будет просто отдавать пользователя
                if user.is_active and user is not None:
                    return user
                else:
                    return None
            else:
                return None
        except:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None