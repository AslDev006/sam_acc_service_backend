from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('contact-us/', ContactCreateView.as_view()),
    path('contact/', AllContactView.as_view()),
    path('called-contact/', CalledContactView.as_view()),
    path('uncalled-contact/', UnCalledContactView.as_view()),
    path('contact/<pk>/', ContactDetailView.as_view()),
]