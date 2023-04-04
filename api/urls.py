from django.urls import path
from .views import CourseListView, CourseDetailView

urlpatterns = [
    
    path("gvp/api/", CourseListView.as_view() ),
    path("gvp/api/<int:pk>", CourseDetailView.as_view() ),
]
