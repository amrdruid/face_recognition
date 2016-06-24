from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^face$', views.face_recognition, name='face_recognition'),
    url(r'^photo$', views.photo, name='photo')
]
