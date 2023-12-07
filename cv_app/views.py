from django.shortcuts import render

def cv_views(request):
    return render(request, 'cv_app/index.html')
