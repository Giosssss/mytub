# mytube/urls.py

from django.contrib import admin
from django.urls import path
from videos import views  # Импортируем views из приложения videos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Главная страница
    path('register/', views.register_view, name='register'),  # Страница регистрации
    path('login/', views.login_view, name='login'),  # Страница входа
    path('profile/', views.profile_view, name='profile'),  # Профиль пользователя
    path('upload_video/', views.upload_video, name='upload_video'),  # Страница загрузки видео
    path('videos/', views.video_list, name='video_list'),  # Список видео
]
