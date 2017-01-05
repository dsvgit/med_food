from rest_framework.routers import DefaultRouter
from api_v0 import views


router = DefaultRouter()
router.register(r'foods', views.FoodViewSet)
router.register(r'users', views.UsersViewSet)
router.register(r'current', views.CurrentUserView, 'current')
# router.register('^user/(?P<username>.+)/$', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = router.urls
