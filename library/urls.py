from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns=[
    path('',views.home,name='home'),
    path('listBooks',views.listBooks,name='listBooks'),
    path('listBooks/create',views.create,name='create'),
    path('listBooks/edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)