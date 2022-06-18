from django.shortcuts import render
from django.http import HttpResponse

from .models import Candidate

# Create your views here.
def index(request):
	candidates = Candidate.objects.all()
	return render(request, 'elections/index.html')

def hobby(request):
	return render(request, 'elections/hobby.html')

def residence(request):
	return render(request, 'elections/residence.html')

def sch_fri(request):
	return render(request, 'elections/sch_fri.html')

def TMI(request):
	return render(request, 'elections/TMI.html')

def travel(request):
	return render(request, 'elections/travel.html')