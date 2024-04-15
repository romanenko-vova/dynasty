from django.shortcuts import render

# Create your views here.

def main(request): 
    return render(request, 'mainapp/index.html')

def family(request):
    return render(request, 'mainapp/family.html')