from rest_framework import routers

from musician.views import MusicianViewSet


router = routers.DefaultRouter()
router.register(r"manage", MusicianViewSet, basename="manage")

urlpatterns = router.urls

app_name = "musician"
