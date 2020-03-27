# posts/urls.py
from django.urls import path
from .views import DiaryList, DiaryDetail


urlpatterns = [
    path('<int:pk>/', DiaryDetail.as_view()),
    path('', DiaryList.as_view()),
]
