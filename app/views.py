from django.shortcuts import render, HttpResponse, redirect
from app.models import *
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from app.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def first1(request):
    if request.user.isanonymous:
        return redirect("/first1")
    return render(request, 'first1.html')
   # return HttpResponse("this is home page")
   
def logina(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/incharge1")
        
    return render(request, 'login1.html')
def login2(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if not User.objects.filter(username=username).exists():
            messages.error(request, "Username does not exist")
        else:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/stud1")
            else:
                messages.error(request, "Incorrect password")
                return render(request, 'login2.html')
    return render(request, 'login2.html')
def register1(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if User.objects.filter(username=username):
            messages.error(request,'Username already taken')
        elif User.objects.filter(email=email):
            messages.error(request,'Email already taken')
        elif password1!=password2:
            messages.error(request,'Passwords doesnot match')
        else:
            User.objects.create_user(username=username,password=password1,email=email)
            return redirect('/login2')

    return render(request,'register1.html',)



def first1(request):
    return render(request,'first1.html',)
@user_passes_test(lambda u:u.is_superuser)
def incharge1(request):
    if 'add' in request.POST:
        room_no=request.POST['room_no']
        if Room.objects.filter(room_no=room_no):
            messages.error(request,"Room already exists")
        else:
            Room(room_no=room_no).save()
            messages.success(request,"Room added")
    if 'delete' in request.POST:
        room_no=request.POST['room_nodel']
        if Room.objects.filter(room_no=room_no):
            Room.objects.get(room_no=room_no).delete()
            messages.success(request,"Room Deleted")
        else :
            messages.error(request,"Room not exist")
    if 'view' in request.POST:
        username=request.POST['username']
        if User.objects.filter(username=username):
            user=User.objects.get(username=username)
            return redirect(f'/stud/{user.id}')
        else:
            messages.error(request,"Student not exist")  
    if 'complaint' in request.POST:
        return redirect('/complaints')        
    return render(request,'incharge1.html',)
def complaints(r):
    com=Complaint.objects.all()
    return render(r,'complaints.html',{'com':com})
def view(r,id):
    stud=User.objects.get(id=id)

    
    room=Book.objects.get(student_id=id)
    return render(r,'view.html',{'stud':stud,'room':room})
def stud1(r):
    if 'view' in r.POST:
        return redirect('/vacant') 
    if 'book' in r.POST:
        room_no=r.POST['room_no']
        if Room.objects.filter(room_no=room_no):
            room=Room.objects.get(room_no=room_no)
            if room.vacant!=0:
                room.vacant-=1
                room.save()
                user=r.user
                Book(student=user,room=room).save()
                messages.success(r,"Room booked successfully")
            else:
                messages.error(r,'Room is full')
        else:
            messages.error(r,'Room doesnot exists')
    if 'complaint' in r.POST:
        name=r.POST['name']
        Complaint(student=r.user,complaint=name).save()
        messages.success(r,'Complaint registered')
    return render(r,'stud1.html')
def vacant(r):
    room=Room.objects.order_by('room_no')
    return render(r,'vacant.html',{'room':room})
def exp(request):
    return HttpResponse("this is home page")
def res(request):
    s=User.objects.order_by('email')
    return render(request,"loginop.html",{'login1':s})

def signout(request):
    logout(request)
    return redirect('/')

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:login1")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="app/register1in.html", context={"register_form":form})