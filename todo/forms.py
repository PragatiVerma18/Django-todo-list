from django import forms

class todoform(forms.Form):
  text = forms.CharField(max_length=40, 
        widget=forms.TextInput(
            attrs={'class' : 'input', 'placeholder' : 'Enter task...', 'type':'text'}))

