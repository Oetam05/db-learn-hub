from .models import Course, Lesson, Exercise
from rest_framework import viewsets, permissions
from .serializers import CourseSerializer, LessonSerializer, ExerciseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CourseSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LessonSerializer

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()    
    permission_classes = [permissions.AllowAny]
    serializer_class = ExerciseSerializer

