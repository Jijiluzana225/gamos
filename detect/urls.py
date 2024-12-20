from django.urls import path
from .views import landing, video_feedx, contact

urlpatterns = [
    path('', landing, name='landing'),  # Landing page
    path('video_feed/', video_feedx, name='video_feed1'),  # Video feed
    path('contact/', contact, name='contact'),  # Contact page
]
