
from django.urls import path
from todo_list import views
urlpatterns = [
    path('', views.home, name = "home.html"),
    path('about', views.about, name = "about.html"),
    path('delete/<list_id>', views.delete, name="delete"),
    path('cross/<list_id>', views.cross, name="cross"),
    path('uncross/<list_id>', views.uncross, name="uncross"),
    path('edit/<list_id>', views.edit, name="edit.html"),
    
]