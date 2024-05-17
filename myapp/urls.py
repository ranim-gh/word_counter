from django.urls import path 
from . import views 

# url config  , URLconf
# url module , every app has a url configuration 




urlpatterns = [
    path('',views.say_hello),
    path('counter/', views.counter, name="counter")
]

     

