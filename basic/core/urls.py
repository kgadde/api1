from django.conf.urls import include, url
from django.contrib import admin

from core.views import save_embed

urlpatterns = {
    url(r'^core/$', save_embed, name="core"),
}

