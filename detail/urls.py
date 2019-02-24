from django.urls import path
from . import views

app_name = "details"
urlpatterns=[
    path('',views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("mypage/", views.mypage, name="mypage"),
    path("qna/", views.qna, name="qna"),
    path("<str:not_found>/", views.error, name="error"),
    ]