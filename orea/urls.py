# -*- coding: utf-8 -*-
"""orea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
import autocomplete_light.shortcuts as al
al.autodiscover()
from rest_framework import routers
from django.contrib import admin

from defcdb import views
router = routers.DefaultRouter()
router.register(r'dc_country', views.DC_countryViewSet)
router.register(r'dc_region', views.DC_regionViewSet)
router.register(r'dc_province', views.DC_provinceViewSet)



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^defcdb/', include('defcdb.urls', namespace="defcdb")),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^accounts/login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
]

