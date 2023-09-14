
from django.shortcuts import render, redirect
from .forms import NameForm

# Create your views here.
def index(request):
	return render(request, 'index.html', {})

def properties(request):
	return render(request, 'propertyapp/properties.html', {})


def about(request):
	return render(request, 'about.html', {})

def services(request):
	return render(request, 'propertyapp/services.html', {})

def contact (request):
	return render(request, 'contact.html', {})





def form(request):
	sample_form = NameForm()
	diction = {'sample_form': sample_form}

	if request.method == "POST":
		sample_form = NameForm(request.POST)
		if sample_form.is_valid():
			your_name = sample_form.cleaned_data['your_name']
			your_dob = sample_form.cleaned_data['your_dob']
			your_email = sample_form.cleaned_data['your_email']

			diction.update({'your_name': your_name})
			diction.update({'your_dob': your_dob})
			diction.update({'your_email': your_email})
			diction.update({'form_submitted':'Yes'})

	return render(request, 'userapp/form.html', context=diction)
