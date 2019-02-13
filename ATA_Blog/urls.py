from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.pageblog, name='blog'),
    path('form/', views.form, name='form'),
    path('blog/<int:post_id>/', views.detail_post, name='detail_post')
]
