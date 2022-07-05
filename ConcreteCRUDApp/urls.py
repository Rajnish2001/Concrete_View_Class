from django.urls import path,include
from .import views

urlpatterns = [
    path('student/',views.StudentListCreate.as_view()),
    path('student/<int:pk>/',views.StudentRetrieveUpdateDestroy.as_view()),
]
