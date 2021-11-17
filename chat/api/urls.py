from django.urls import path, re_path
from .views import (ChatListView, ChatCreateView, ChatDetailView, ChatDeleteView,ChatUpdateView)

app_name = 'chat'

urlpatterns = [
    path('', ChatListView.as_view()),
    path('create/', ChatCreateView.as_view()),
    path('<pk>', ChatDetailView.as_view()),
    path('<pk>/update/', ChatUpdateView.as_view()),
    path('<pk>/delete/', ChatDetailView.as_view())
]
