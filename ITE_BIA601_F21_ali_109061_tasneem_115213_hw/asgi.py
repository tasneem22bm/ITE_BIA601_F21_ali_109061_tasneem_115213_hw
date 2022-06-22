"""
ASGI config for ITE_BIA601_F21_ali_109061_tasneem_115213_hw project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ITE_BIA601_F21_ali_109061_tasneem_115213_hw.settings')

application = get_asgi_application()
