from django.shortcuts import render

def index(request) :
    return render(request, 'personal/home.html')

def contact(request) :
    return render(request, 'personal/basic.html', {'content' : ['Telefon: +48 799 931 323','Email: pawel.wong@gmail.com']})

def us(request) :
    return render(request, 'personal/us.html')

def offer(request) :
    return render(request, 'personal/offer.html')

def partners(request) :
    return render(request, 'personal/partners.html')

def gethelp(request) :
    return render(request, 'personal/gethelp.html')