from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.

# to add and display the data
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw) #if you dont want to save any of the entry then you can remove it from this function and that step also
            reg.save()
            fm = StudentRegistration()
            # fm.save() #alteranate method if we dont want a lengthy process (remove nm, em, pw, reg lines)
    else:
        fm = StudentRegistration()
    stu = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stu})

# to update and edit data
def update_data(request, id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        fm= StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm= StudentRegistration(instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form': fm})

# to delete the data
def delete_data(request, id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id) # pk= primary key
        pi.delete()
        return HttpResponseRedirect('/')