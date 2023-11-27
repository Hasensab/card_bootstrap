from django.shortcuts import render

# Create your views here.
def card(request):
    return render(request,'card.html')
def card1(request):
    return render(request,'card1.html')
def card2(request):
    return render(request,'card2.html')