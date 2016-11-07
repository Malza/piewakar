from django.shortcuts import render

def index(request) :
    return render(request, 'personal/home.html')

def contact(request) :
    return render(request, 'personal/basic.html', {'content' : ['Telefon: +48 799 931 323','Email: pawel.wong@gmail.com']})