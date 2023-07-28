from django.contrib import admin
from django.urls import path,include
from api.views import CompanyviewSet
from rest_framework import routers

router= routers.DefaultRouter()
router.register(r'companies', CompanyviewSet)

urlpatterns = [
    path('', include(router.urls))
]
