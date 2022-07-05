from django.urls import path
from .import views

urlpatterns = [
    path('studentlist/',views.StudentList.as_view()),
    path('studentcreate/',views.StudentCreate.as_view()),
    path('studentretrieve/<int:pk>/',views.StudentRetrieve.as_view()),
    path('studentupdate/<int:pk>/',views.StudentUpdate.as_view()),
    path('studentdestroy/<int:pk>/',views.StudentDestroy.as_view()),
    path('studentlistcreate/',views.StudentListCreate.as_view()),
    path('studentretrieveupdate/<int:pk>/',views.StudentRetrieveUpdate.as_view()),
    path('studentretrievedestroy/<int:pk>/',views.StudentRetrieveDestroy.as_view()),
    path('studentretrieveupdatedestroy/<int:pk>/',views.StudentRetrieveUpdateDestroy.as_view()),
]
