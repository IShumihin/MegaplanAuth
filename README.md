### Django auth from [Megaplan](https://megaplan.ru/)

- Add MEGAPLAN_AUTH_HOST in you settings.py and set megaplan url
- Add 'MegaplanAuth.MegaplanAuthBackends' in you AUTHENTICATION_BACKENDS

#### Options 
MEGAPLAN_AUTH_GREATE_USER(default: True) - create a new user if the user is not found but it authorization

MEGAPLAN_AUTH_USER_ACTIVE(default: True) - mark new user as active if True

MEGAPLAN_AUTH_SUPER_USER_IDS - users ids list to mark as superuser

MEGAPLAN_AUTH_STAF_USER_IDS - users ids list to mark as staff