from django.conf import settings
from django.shortcuts import render, redirect
from django.views import View
from .models import Contact
from .forms import ContactForm, ContactEditForm
from django.shortcuts import get_object_or_404

import os


class StartPage(View):
    def get(self, request):
        return render(request, 'contacts/start_page.html')

class CreateContact(View):
    template_name = 'contacts/create_contact.html'

    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            return redirect('contact_management')
        return render(request, self.template_name, {'form': form})

class ContactManagement(View):
    def get(self, request):
        contacts = Contact.objects.all()
        return render(request, 'contacts/contact_management.html', {'contacts': contacts})

class ContactDetail(View):
    def get(self, request, pk):
        contact = Contact.objects.get(pk=pk)
        return render(request, 'contacts/contact_detail.html', {'contact': contact})

class ContactEdit(View):
    template_name = 'contacts/contact_edit.html'

    def get(self, request, pk):
        contact = get_object_or_404(Contact, pk=pk)
        form = ContactEditForm(instance=contact)
        return render(request, self.template_name, {'form': form, 'contact': contact})

    def post(self, request, pk):
        contact = get_object_or_404(Contact, pk=pk)
        form = ContactEditForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_detail', pk=contact.pk)
        else:
            return render(request, self.template_name, {'form': form, 'contact': contact})


class ContactDelete(View):
    template_name = 'contacts/contact_delete.html'

    def get(self, request, pk):
        contact = get_object_or_404(Contact, pk=pk)
        return render(request, self.template_name, {'contact': contact})

    def post(self, request, pk):
        contact = get_object_or_404(Contact, pk=pk)
        contact.delete()
        return redirect('contact_management')

