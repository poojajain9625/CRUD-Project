from django.shortcuts import render, HttpResponsePermanentRedirect
from .forms import StudentRegisteration
from .models import User
from django.contrib import messages

# This function will add new Item and Show all Items
def add_show(request):
    if request.method == 'POST':
        fm=StudentRegisteration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pd=fm.cleaned_data['password']
            reg=User(name=nm, email=em, password=pd)
            reg.save()
            fm=StudentRegisteration()
    else:
        fm=StudentRegisteration()
    stud=User.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm, 'stu':stud})


# This function will Edit/Update
def update_data(request, id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        fm=StudentRegisteration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.add_message(request, messages.SUCCESS,'Your account has been created Successfully!!!')
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegisteration(instance=pi)
    return render(request,'enroll/updatestudent.html', {'form':fm})

# This function will delete 
def delete_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponsePermanentRedirect('/')