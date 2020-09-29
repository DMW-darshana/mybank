from django import forms

class LoginForm(forms.Form):
    loginid=forms.CharField(label='loginid',max_length=20)
    password=forms.CharField(label='password',max_length=20,widget=forms.PasswordInput())
    