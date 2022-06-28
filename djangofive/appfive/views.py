from xml.dom.domreg import registered
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm, UserProfileInfoForm
from django.urls import URLResolver, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def index(request):
    return render(request, 'appfive/index.html')

@login_required
def special(request):
    return HttpResponse('You are logged in')



@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect(reverse('index'))


def register(request):
    resgistered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            #hashing password
            user.set_password(user.password) 
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            print('user saved')

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()

            resgistered = True
            


        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    context= {
        'user_form':user_form,
        'profile_form': profile_form,
        'registered': resgistered,
    }

    return render(request, 'appfive/registration.html', context=context)

def base(request):
    return render(request, 'appfive/base.html')




def user_login(request):

    if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')

         user = authenticate(username=username, password=password)
         if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account Not Active')
         else:
            print('Someone tried to login and failed')
            return HttpResponse('Invalid login details')
    else:
        return render(request, 'appfive/login.html')

