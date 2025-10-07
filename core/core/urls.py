from django.contrib import admin
from django.urls import path
from vege import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.recipe_list, name='recipe_list'),   # homepage
    path('update/<int:recipe_id>/', views.update_recipe, name='update_recipe'),
    path('delete/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
]

# for images
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

