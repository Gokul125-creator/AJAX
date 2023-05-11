from django.shortcuts import render
from .models import Login


def home(request):
	ids = Login.objects.all()
	return render(request, 'login.html', {"ids":ids})
