from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import random

# Create your views here.
def hello(request):
    result={
        "message":"123",
        "number":"456",
        "data":"789",
    }
    return JsonResponse(result)

def lottory(request):
    spec_number = 0
    numbers = sorted(random.sample(range(1,50),6))
    while spec_number in numbers or spec_number == 0:
        spec_number = random.randint(1,49)
    numbers = " ".join([str(i) for i in numbers])
    result = {"numbers":numbers,
              "spec_number":spec_number,
              }
    
    return render(request,"lottory.html",result)
    #return JsonResponse(result)

