from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
import json

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        # Store the username and password in the database
        user = User.objects.create(username=username, password=password)

        return JsonResponse({'message': 'Login successful'}, status=200)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

# Create your views here.
