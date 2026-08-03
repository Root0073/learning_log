from django.urls import path
from . import views
app_name = 'learning_logs'
urlpatterns = [
    #主页
    path(r'', views.index, name='index'),
    path(r'^topics/$', views.topics, name='topics'),
    path(r'^topics/(?P<topic_id>\d+)/$', views.topics, name='topic')
]
