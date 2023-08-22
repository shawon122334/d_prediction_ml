import os

import joblib as joblib
import numpy as np


from .models import Medical, Ment, Profile, User


def about(request):
	return render(request, 'about.html')


def doctor_list(request):
	return render(request, 'doctors.html')


def home(request):
	return render(request, 'home.html')


def registerView(request):
	return render(request, 'register.html')


def registerUser(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		password = make_password(password)

		
	else:
		

