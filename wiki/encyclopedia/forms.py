from django import forms

class title(forms.Form):
    title = forms.CharField(label='title', max_length=100)

class post(forms.Form):
    title = forms.CharField( max_length=100)
    content = forms.CharField(widget=forms.Textarea)