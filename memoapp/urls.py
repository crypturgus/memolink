from django.conf.urls import url

from memoapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]