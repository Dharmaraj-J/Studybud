from django.shortcuts import render


# Create your views here.

rooms = [
    {'id':1, 'name':'let learn python'},
    {'id':2, 'name':'Desingn with me'},
    {'id':3, 'name':'Frontend Developers'},
]

def home(request):
    return render(request,'home.html',{'rooms':rooms})

def room(request):
    return render(request,'room.html')