from django.conf.urls import url
from . import views

app_name = 'import'

urlpatterns = [
    # /photos/
    url(r'^$', views.index, name='index'),
]
