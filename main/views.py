from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Chika Marsya Diandra Lumban Gaol',
        'class': 'PBP F '
    }

    return render(request, "main.html", context)
# Create your views here.
