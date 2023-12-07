from django.urls import path
from .views import *

app_name = 'CV'

urlpatterns = [
    path('',cv_views,name='cv'),
]
