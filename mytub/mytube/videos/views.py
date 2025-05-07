from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Video  # если используешь модель Video
from .forms import VideoUploadForm  # если создашь форму загрузки

# Главная страница
def index(request):
    return render(request, 'videos/index.html')

# Регистрация
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'videos/register.html', {'form': form})

# Вход
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Неверные данные.')
    else:
        form = AuthenticationForm()
    return render(request, 'videos/login.html', {'form': form})

# Профиль пользователя
@login_required
def profile_view(request):
    return render(request, 'videos/profile.html')

# Загрузка видео (только для учителей)
@login_required
def upload_video(request):
    if not request.user.groups.filter(name='Учителя').exists():
        messages.error(request, 'Только учителя могут загружать видео.')
        return redirect('index')

    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.author = request.user
            video.save()
            messages.success(request, 'Видео загружено!')
            return redirect('profile')
    else:
        form = VideoUploadForm()
    return render(request, 'videos/upload_video.html', {'form': form})

# Просмотр видео
def video_list(request):
    videos = Video.objects.all()
    return render(request, 'videos/video_list.html', {'videos': videos})
