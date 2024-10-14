from django.shortcuts import render
def home(request):
    return render(request,'first_app/index.html',{'title':'Home'});
# from django.http import HttpResponse
# 
# def home(request):
#     return HttpResponse("now working...")

# Create your views here.
