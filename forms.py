from django import forms
class MyForm(forms.Form):
    username=forms.CharField(label="username",max_length=100)
    password=forms.CharField(label="password",widget=forms.PasswordInput)
    phone_no=forms.IntegerField(label="phone_no")
    address=forms.CharField(label="username",max_length=100)
    