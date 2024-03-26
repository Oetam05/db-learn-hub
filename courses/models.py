from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self): return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    def __str__(self): return self.title


class Exercise(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    question = models.JSONField()
    solution = models.JSONField()
    points = models.IntegerField(default=0)
    hint = models.TextField(blank=True, null=True)
    difficulty = models.CharField(max_length=10, choices=[(
        'Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')])  # Dificultad del ejercicio
    type = models.CharField(max_length=20, choices=[('MCQ', 'Multiple Choice Question'), (
        'Code', 'Code'), ('Fill', 'Fill in the Blank')])  # Tipo de ejercicio
