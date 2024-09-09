from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth import login , logout , authenticate 
from django.contrib import messages
from .forms import SignUpForm , AddRecordForm
from .models import Record


def home ( request):

    if request.method == 'POST':
        username = request.POST ['username']
        password = request.POST ['password']
        user = authenticate(request , username = username , password = password)

        if user is not None :
            login(request , user)
            messages.success( request , "you have been logged in ")
            return redirect ('home')
        else :
            messages.success(request , "login failed , please try again")

    records = Record.objects.all()
    return render (request , 'home.html' , {'records' : records})

def logout_user (request):
    logout(request)
    messages.success(request , 'you have been logged out ...')
    return redirect ('home')

def register_user (request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username , password = password)
            login(request , user)
            messages.success(request , 'you have been registered')
            return redirect ('home')
        else :
            return render (request , 'register.html' , {'form' : form})

    else :
        form = SignUpForm()
        return render (request , 'register.html' , {'form' : form})

def record (request , id):
        if (request.user.is_authenticated):
            record = Record.objects.get(id=id)
            return render (request , 'record.html' , {'record' : record})   
        else :
             messages.success(request , 'you must be logged in to view this record ..')
             return redirect ('home')
        
def delete_record (request , id):
        if (request.user.is_authenticated):
            record = Record.objects.get(id=id)
            record.delete()   
            messages.success(request , 'record deleted ..')
            return redirect ('home')
        else :
             messages.success(request , 'you must be logged in to view this record ..')
             return redirect ('home')
         

def add_record (request):
      if request.user.is_authenticated:
           form = AddRecordForm(request.POST or None)
           if request.method == 'POST':
                if (form.is_valid):
                     form.save()
                     messages.success(request , "record added successfully")
                     return render (request , "add_record.html" , {"form" : AddRecordForm(None)})
                else :
                      messages.success(request , "form is not vaild")
                      return render (request , 'add_record.html' , {"form":form})
           else :
                return render (request , 'add_record.html' , {"form":form})
      else:
           messages.success(request , "you must be logged in")
           return redirect ("home")

def update_record(request , id):
     if request.user.is_authenticated:
           prev_record = Record.objects.get(id=id)
           form = AddRecordForm(request.POST or None , instance=prev_record) 
           if request.method == 'POST':
                if (form.is_valid):
                     form.save()
                     messages.success(request , "record updated successfully")
                     print(id)
                     return redirect("/record/"+id)
                else :
                      messages.success(request , "form is not vaild")
                      return render (request , 'update_record.html' , {"form":form})
           else :
                return render (request , 'update_record.html' , {"form":form})
     else:
           messages.success(request , "you must be logged in")
           return redirect ("home")
     


                     
    
       
       

   

    
   

