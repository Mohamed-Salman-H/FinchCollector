from django.shortcuts import render
from django.http import HttpResponse
from .models import Finch


def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', {'finch': finch})



def finches_index(request):
    finches_list = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finches_list
    })


def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')