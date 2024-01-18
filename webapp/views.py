from django.shortcuts import redirect, render
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .models import Record


#  - Home
def home(request):
    return render(request, 'webapp/index.html')




#  - Register

def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('my-login')

    context = {'form': form}

    return render(request, 'webapp/register.html', context=context)


#  - Login 
def myLogin(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data = request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                auth.login(request, user)

                return redirect('dashboard')

    context = {'form': form}

    return render(request, 'webapp/my-login.html', context = context)




#  - Dashboard

@login_required(login_url = 'my-login')
def dashboard(request):

    my_records = Record.objects.all()

    context = {'records':my_records}

    return render(request, 'webapp/dashboard.html', context=context)



#  - logout

def useLogout (request):
    auth.logout(request)

    return redirect('my-login')

#  - create a record

@login_required(login_url='my-login')
def create_record(request):
    form = CreateRecordForm()

    if request.method == "POST":
        form = CreateRecordForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('dashboard')
    context = {'form' : form}

    return render(request, 'webapp/create-record.html', context=context)



#  - update a record

@login_required(login_url='my-login')
def update_record(request, pk):
    
    record = Record.objects.get(id = pk)

    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record )

        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': form }
    return render(request, 'webapp/update-record.html', context=context)



#  - Read/View Singular Recorrd
@login_required(login_url='my-login')
def record(request, pk):
    all_records = Record.objects.get(id=pk)

    return render(request, 'webapp/view-record.html', {'record':all_records})



#  - Delete a Record
@login_required(login_url='my-login')
def delete_record(request, pk):
    record = Record.objects.get(id=pk)

    record.delete()

    return redirect('dashboard')