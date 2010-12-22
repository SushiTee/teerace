from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.generic.list_detail import object_list
from accounts.forms import LoginForm, RegisterForm
from accounts.models import UserProfile
from annoying.functions import get_config
from annoying.decorators import render_to


@render_to('accounts/login.html')
def login(request):
	if request.user.is_authenticated():
		return redirect(reverse('home'))

	next_uri = request.REQUEST.get('next', get_config('LOGIN_REDIRECT_URL',
		reverse('accounts.views.welcome')))
	# rescuing poor users from infinite redirection loop
	if next_uri == get_config('LOGIN_URL', reverse('login')):
		next_uri = get_config('LOGIN_REDIRECT_URL', reverse('accounts.views.welcome'))

	login_form = LoginForm()

	if request.method == 'POST':
		login_form = LoginForm(request.POST)
		if login_form.is_valid() and login_form.user:
			auth_login(request, login_form.user)
			messages.success(request, "Hello, {0}.".format(login_form.user))
			return redirect(next_uri)

	return {
		'login_form': login_form,
		'next': next_uri,
	}


@login_required
def logout(request):
	next_uri = request.REQUEST.get('next', reverse('home'))
	auth_logout(request)
	messages.success(request, "Bye bye.")
	return redirect(next_uri)


@render_to('accounts/register.html')
def register(request):
	if request.user.is_authenticated():
		return redirect(reverse('home'))

	next_uri = request.REQUEST.get('next', get_config('FIRST_LOGIN_REDIRECT_URL',
		reverse('accounts.views.first_steps')))
	# rescuing poor users from infinite redirection loop
	if next_uri == get_config('LOGIN_URL', reverse('login')):
		next_uri = get_config('FIRST_LOGIN_REDIRECT_URL',
			reverse('accounts.views.first_steps'))

	register_form = RegisterForm()

	if request.method == 'POST':
		register_form = RegisterForm(request.POST)
		if register_form.is_valid():
			auth_login(request, register_form.save())
			messages.success(request, "Welcome aboard, {0}.".format(register_form.user))
			redirect(next_uri)

	return {
		'register_form': register_form,
		'next': next_uri,
	}


@render_to('accounts/first_steps.html')
def first_steps(request):
	return {

	}


@render_to('accounts/welcome.html')
def welcome(request):
	return {

	}


def profile(request, user_id):
	profiles = UserProfile.objects.all().select_related()
	return object_detail(request, queryset=entries, object_id=user_id,
		paginate_by=get_config('ITEMS_PER_PAGE', 20))
	

def userlist(request):
	profiles = UserProfile.objects.all().select_related()
	return object_list(request, queryset=profiles, paginate_by=get_config('ITEMS_PER_PAGE', 20))
