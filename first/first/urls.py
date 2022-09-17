from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (TokenRefreshView,TokenObtainPairView )
from rest_framework.routers import DefaultRouter
from login.views import UserViewSet
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
router=DefaultRouter()
router.register('user',UserViewSet,basename='user')
urlpatterns+=router.urls