from django.shortcuts import render
import math

# Create your views here.
def fact(request):
    if request.method == 'POST':
        f = request.POST.get('fact')
        fact = math.factorial(int(f))
        print("factorial", fact)
        return render(request, 'index.html', {'fact':fact})
    else:
        return render(request, 'index.html')