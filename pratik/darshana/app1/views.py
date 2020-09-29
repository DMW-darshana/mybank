from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Users
from app1.forms import LoginForm
def index(request):
	fobj=LoginForm
	return render(request,'index.html',{'form':fobj})

def message(request):
	mess=' this is my message page'
	return render(request,'message.html',{'message':mess})

def checklogin(request):
	if request.method=='POST':
		tlogin=request.POST.get('loginid')
		tpass=request.POST.get('password')	
		uobj=Users(loginid=tlogin,password=tpass)
		uobj.save()
		return HttpResponse('Data Entered Successful')
# Create your views here.
