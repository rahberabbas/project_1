from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apis.urls')),
    path('stripe_api/', include('stripe_api.urls')),
]
