from django.urls import path,include
from . import views

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', include('django.contrib.auth.urls'), name='logout'),
    path('', views.index, name='index'),
]
