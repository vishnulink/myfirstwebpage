from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('http://127.0.0.1:5500/Saas-Website/login.html', include('login_app.urls')),
]