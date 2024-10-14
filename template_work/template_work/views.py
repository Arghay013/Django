from django.shortcuts import render

def template_home(request):
    return render(request,'index.html');