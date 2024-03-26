from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('api/course', CourseViewSet, 'course')
router.register('api/lesson', LessonViewSet, 'lesson')
router.register('api/exercise', ExerciseViewSet, 'exercise')


urlpatterns = router.urls