from django import forms
from vehicle_managementweb.models import User,Vehicles
from django.contrib.auth.forms import UserCreationForm




class RegistrationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control border border-primary ","placeholder":"enter password"}))  
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control border border-primary","placeholder":"confirm password"}))              
    
    class Meta:
        model=User
        fields=['username','email','role']

        widgets={
            "username":forms.TextInput(attrs={"class":"form-control border border-primary","placeholder":"enter username"}),
            "email":forms.EmailInput(attrs={"class":"form-control border border-primary","placeholder":"enter email"}),
            "role":forms.Select(attrs={"class":"form-select form-control border border-primary"})
        } 
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

    
class VehicleForm(forms.ModelForm):
    class Meta:
        model=Vehicles
        fields=["vehicle_number",'vehicle_type','vehicle_model',"vehicle_description"]
        
        widgets={
            "vehicle_number":forms.TextInput(attrs={"class":"form-control",'pattern':'[A-Za-z0-9]+','title':'Enter Alphanumeric Characters Only A-Z,a-z,0-9 ',"placeholder":"enter vehicle number"}),
            "vehicle_model":forms.TextInput(attrs={"class":"form-control","placeholder":"enter vehicle model"}),
            "vehicle_description":forms.TextInput(attrs={"class":"form-control","placeholder":"enter vehicle description"}),
            "vehicle_type":forms.Select(attrs={"class":"form-select form-control"})
        } 
