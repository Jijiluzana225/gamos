from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),  # Landing page
    path('video_feed/', views.video_feedx, name='video_feed1'),  # Video feed
    path('contact/', views.contact, name='contact'),  # Contact page
]
