from django.urls import path, include
from rest_framework import routers
from .views import *
from .routers import CustomReadOnlyRouter



router = routers.DefaultRouter()
router_dinc = CustomReadOnlyRouter()
router.register(r'personels', PersonalMVS)
router.register(r'', DepartmantGetMVS)
router_dinc.register(r'departments', DepartmantDinamicMVS)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router_dinc.urls)),
]
# urlpatterns = router.urls
# urlpatterns += router_dinc.urls