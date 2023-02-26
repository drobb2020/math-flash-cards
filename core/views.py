from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'core/index.html', context)
