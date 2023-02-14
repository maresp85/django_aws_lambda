from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path

from page.views import page, page2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', page2),
    path('', page),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)