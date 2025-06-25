# #Create URLS FILE
# from django.urls import path
# from .views import bus_list

# urlpatterns = [
#     path('api/buses/', bus_list, name='bus-list'),
# ]

from django.urls import path
from .views import bus_list, create_booking, RegisterView
from django.http import JsonResponse
def api_root(request):
    return JsonResponse({"message": "Welcome to the API"})

urlpatterns = [
    path('', api_root),  # This handles /api/
    path('buses/', bus_list),
    path('book/', create_booking),
    path('register/', RegisterView.as_view()),
]