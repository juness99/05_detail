from django.shortcuts import render
# from .models import Detail
# Create your views here.
def index(request):
    return render(request,"detail/index.html")
    
def signup(request):
    return render(request, "detail/signup.html")
    
def mypage(request):
    return render(request, "detail/mypage.html")
    
def qna(request):
    return render(request, "detail/qna.html")
    
def error(request, not_found):
    return render(request, "detail/error.html", {"not_found":not_found})