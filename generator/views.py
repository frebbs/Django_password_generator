from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(req):
    return render(req, 'generator/home.html')


def password(req):

    generated_password = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(req.GET.get('length', 14))


    if req.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))


    if req.GET.get('special'):
        characters.extend(list('!@€£#$%^&*()?/.<,~`±§'))


    if req.GET.get('numbers'):
        characters.extend(list('1234567890'))


    for x in range(length):
        generated_password += random.choice(characters)


    return render(req, 'generator/password.html', {
        'password':  generated_password
    })


def about(req):
    return render(req, 'generator/about.html')