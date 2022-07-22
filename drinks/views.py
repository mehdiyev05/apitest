from django.http import JsonResponse,HttpResponse
from .models import Drink
from .serializers import DrinkSerializer

def drink_list(request):

    drinks=Drink.objects.all()
    serializer=DrinkSerializer(drinks,many=True)
    return JsonResponse(serializer.data,safe=False)



def home(request):
    return HttpResponse('<h1>Vuqar agilli ol</h1>')    