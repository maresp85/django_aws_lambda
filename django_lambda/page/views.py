from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def page(request):
    name = 'PRUEBA LAMBDA: FORM'
    if request.method == 'POST':
        name = request.POST.get('name', '')
    return render(request, 'index.html', {'name': name})


def page2(request):
    return HttpResponse('PAGINA NUMERO 2', content_type='text/plain')