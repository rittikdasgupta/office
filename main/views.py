from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'main/index.html')

def contact(request):
    return render(request, 'main/contact.html')
def webdesign(request):
    return render(request,'main/wb.html')