from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('posts', views.PostViewSet)
router.register('profile', views.ProfileViewSet)

urlpatterns=[
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
    path('(?P<username>\w+)/profile/', views.user_profile, name='userprofile'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('profile/(?P<username>\w+)',views.profile,name='profile'),
    path('profile/(?P<username>\w+)/settings', views.edit_profile, name='edit'),
    path('project/(?P<post>\w+)', views.project, name='project'),
    path('search/', views.search_project, name='search'),
    path('postImage/',views.post_image,name='postImage'),
]
