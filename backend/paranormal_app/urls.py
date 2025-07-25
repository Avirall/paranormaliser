from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courage_interface.urls')),
    path('ai/', include('ai_integration.urls')),
]
