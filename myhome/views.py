from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'hello.html', {})

def nong(request):
    return render(request, 'nong.html', {})

def mul(request):
    return render(request, 'betafish.html', {})