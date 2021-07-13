from django.urls import path
from .views import CompanyApiView

urlpatterns=[
    path('data',CompanyApiView.as_view(),name='company_api_view')
]