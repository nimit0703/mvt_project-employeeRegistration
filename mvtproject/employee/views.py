from django.shortcuts import render,HttpResponsePermanentRedirect

from .forms import EmployeeResgitration
from .models import User

# Create your views here.


# to add and show data 
def add_show(request):
    if request.method == 'POST':
        fm = EmployeeResgitration(request.POST)
        if fm.is_valid():
            nm= fm.cleaned_data['name']
            em= fm.cleaned_data['email']
            pw= fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm=EmployeeResgitration()
    else:
        fm = EmployeeResgitration()
    empl = User.objects.all()

    return render(request, 'employee/addandshow.html', {'form' : fm, 'emp':empl})


# to delete data 
def delete_data(request,id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponsePermanentRedirect('/')