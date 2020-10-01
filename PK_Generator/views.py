from django.shortcuts import render
import random

# Create your views here.

def home(request):
    return render(request, 'PK_Generator/home.html')

def password(request):
    
    characters = []
    
    length = int(request.GET.get('length', 10)) # take 10 as a default value
    
    if request.GET.get('lowercase'):
        characters.extend(list('abcdefghijklmnopqrstuvwxyz'))
        
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
        
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
        
    if request.GET.get('excludesimilar'):
        similar = list('iIl|0Oo')
        for char in similar:
            if char in characters:
                characters.remove(char)
    
    password = ''
    if characters:
        for i in range(length):
            password += random.choice(characters)
    
    return render(request, 'PK_Generator/password.html', {'password':password})