from django.shortcuts import render, HttpResponse
from home.models import Help
from datetime import datetime
from django.contrib import messages



# Create your views here.

def index(request):
    context = {
        "variable" : "Hi Brotehers"
    }
    
    return render(request, 'index.html')
    # return HttpResponse("This is the ")

def about(request):
    return render(request, 'About.html')
def members(request):
    return render(request, 'members.html')

def help(request):
    if request.method == "POST" :
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        help = Help(name = name, email = email, desc = desc, date = datetime.today())
        help.save()
        messages.success(request, 'Your message successfully sent.')

    return render(request, 'help.html')






