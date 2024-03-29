"""NB_crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from crm import views
urlpatterns = [

    #公户
    path('customer_list/',views.CustomerList.as_view(),name='customer_list'),
    # path('customer_list/',views.customer_list,name='customer_list'),
    #私户
    path('my_customer/',views.CustomerList.as_view(),name='my_customer'),
    # path('my_customer/',views.customer_list,name='my_customer'),
    #增加客户
    # path('customer/add/',views.add_customer,name='add_customer'),
    # #编辑客户
    # path('customer/edit/<int:nid>/',views.edit_customer,name='edit_customer'),
    path('customer/add/',views.customer,name='add_customer'),
    #编辑客户
    path('customer/edit/<int:nid>/',views.customer,name='edit_customer'),


]
