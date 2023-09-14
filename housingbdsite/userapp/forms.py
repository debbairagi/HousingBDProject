from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)
    your_dob = forms.DateField(label='Date Of Birth', widget=forms.TextInput(attrs={'type':'date'}))
    your_email = forms.EmailField(label="Your Email", max_length=100)