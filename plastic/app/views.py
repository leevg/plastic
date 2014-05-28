from annoying.decorators import render_to

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required

from django.core.urlresolvers import reverse

from django.shortcuts import redirect
from django.template import RequestContext

@render_to('plastic/home.html')
def home(request):
    return {}

@render_to('registration/signup.html')
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return redirect(reverse('home'))
    else:
        form = UserCreationForm()
    return {'form': form}

@render_to('admin/users.html')
def user(request):
    return {'users': User.objects.all()}

user = staff_member_required(user)