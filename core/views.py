from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {
        'name': 'Alexandro Castro'
    }
    return render(request, 'recipes/home.html', context=context)


def about(request):
    return HttpResponse('ABOUT')


def test_base(request):
    return render(request, 'global/base.html')
