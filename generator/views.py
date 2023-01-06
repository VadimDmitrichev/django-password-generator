from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
	return render(request, 'generator/home.html')


def password(request):
	the_password = ''
	characters = list('qwertyuiopasdfghjklzxcvbnm')
	length = int(request.GET.get('length'), 10)

	if request.GET.get('uppercase'):
		characters.extend('QWERTYUIOPASDFGHJKLZXCVBNM')
	if request.GET.get('special'):
		characters.extend('!@#$%^&*')
	if request.GET.get('numbers'):
		characters.extend('1234567890')

	for i in range(length):
		the_password += random.choice(characters)

	return render(request, 'generator/password.html', {'the_password': the_password})


def about(request):
	return render(request, 'generator/about.html')
