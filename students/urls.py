from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, CourseViewSet, EnrollmentViewSet, ResultViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'results', ResultViewSet)

urlpatterns = router.urls