from django.urls import path,include
from ImageCollection import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name = 'Home'),
    path('submit',views.submit,name="submit"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)