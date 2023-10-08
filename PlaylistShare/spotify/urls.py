from django.urls import path
from . import views
from .views import AuthURL,spotify_callback, IsAuthenticated

urlpatterns = [
    # try removing brackets after function if it doesnt work
    path('/get-auth-url',AuthURL.as_view()),
    path('hello/', views.say_hello),
    path('redirect', spotify_callback),
    path('is-authenticated', IsAuthenticated.as_view())
]