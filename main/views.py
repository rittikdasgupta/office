from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'main/index.html')

def mainpage(request):
    return render(request,'main/main.html')

def contact(request):
    return render(request, 'main/contact.html')

def webdesign(request):
    return render(request,'main/wb.html')

def graphicsdesign(request):
    return render(request,'main/graphics.html')

def socialmedia(request):
    return render(request,'main/socialmedia.html')

def team(request):
    return render(request,'main/team.html')
def contact(request):
    return render(request,'main/contact.html')