from django.contrib import admin
from django.urls import path
from contacts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.StartPage.as_view(), name='start_page'),
    path('create/', views.CreateContact.as_view(), name='create_contact'),
    path('contact_management/', views.ContactManagement.as_view(), name='contact_management'),
    path('contact/<int:pk>/', views.ContactDetail.as_view(), name='contact_detail'),
    path('contact/<int:pk>/edit/', views.ContactEdit.as_view(), name='contact_edit'),
    path('contact/<int:pk>/delete/', views.ContactDelete.as_view(), name='contact_delete'),
]
