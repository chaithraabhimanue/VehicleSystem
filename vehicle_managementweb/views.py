from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.views.generic import View,CreateView,FormView,ListView,UpdateView,DeleteView
from vehicle_managementweb.forms import RegistrationForm,LoginForm,VehicleForm
from vehicle_managementweb.models import User,Vehicles
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.cache import never_cache
from django.urls import reverse_lazy


# Create your views here.
def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)    
    return wrapper


def superadmin_required(user):
    return user.is_authenticated and user.role in (1,3)

def admin_or_superadmin_required(user):
    return user.is_authenticated and user.role in (1,2)

decs=[never_cache,signin_required,user_passes_test(admin_or_superadmin_required)]
decs1=[never_cache,signin_required,user_passes_test(superadmin_required)]
decs2=[signin_required,never_cache]


class RegistrationView(CreateView):
    model=User
    form_class=RegistrationForm
    template_name="register.html"
    success_url=reverse_lazy("signin")

class LoginView(FormView):
    form_class=LoginForm
    template_name="login.html"

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("home")
            else:
                return render(request,"login.html",{"form":form})

@method_decorator(decs2,name="dispatch")
class HomeView(CreateView,ListView):
    model=Vehicles
    form_class=VehicleForm
    template_name='home.html'
    context_object_name="vehicle"
    success_url=reverse_lazy("home")

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
@method_decorator(decs2,name="dispatch")
class Addvehicleview(CreateView):
    model=Vehicles
    form_class=VehicleForm
    template_name="add-vehicledetails.html"
    success_url=reverse_lazy("home")
    
@method_decorator(decs,name="dispatch")
class Edit_vehicledetailsView(UpdateView):
    model=Vehicles
    form_class=VehicleForm
    template_name="vehicledetails-edit.html"
    success_url=reverse_lazy("home")
    pk_url_kwarg="id"


@method_decorator(decs1,name="dispatch")
class VehicleDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Vehicles.objects.filter(id=id).delete()
        return redirect("home")
    
    
@method_decorator(decs2,name="dispatch")
class Signoutview(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")
    

