from django.conf.urls import url
# import the views module from the posts app
from posts import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
