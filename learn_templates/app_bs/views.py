from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict={'text':'Hello World', 'number':100}
    return render(request, 'app_bs/index.html', context_dict)

def other(request):
    return render(request, 'app_bs/other.html')

def relative(request):
    return render(request, 'app_bs/relative_url.html')