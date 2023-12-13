from django.urls import path
from .views import StartPage, CreateContact, ContactManagement, ContactDetail, ContactEdit, ContactDelete

urlpatterns = [
    path('', StartPage.as_view(), name='start_page'),
    path('create/', CreateContact.as_view(), name='create_contact'),
    path('manage/', ContactManagement.as_view(), name='contact_management'),
    path('detail/<int:pk>/', ContactDetail.as_view(), name='contact_detail'),
    path('edit/<int:pk>/', ContactEdit.as_view(), name='contact_edit'),
    path('delete/<int:pk>/', ContactDelete.as_view(), name='contact_delete'),
]
