from django.shortcuts import render, render_to_response, HttpResponse
from django.http import HttpResponse
from .models import Article
from django.db.models import Q
from django import forms
from .models import User
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def index(request):
	names = Article.objects.all()
	return render(request, 'index.html',locals())

@login_required
def search(request):
	q = request.GET.get('q')
	error_msg=''
	if not q:
		error_msg = '请输入关键词'
		return render(request, 'index.html', {'error_msg': error_msg})
	
	post_list = Article.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))
	username = req.COOKIES.get('username', '')
	return render(request, 'index.html', {'error_msg': error_msg, 'post_list': post_list})

class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=50)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())
    email = forms.EmailField(label='邮箱')

def regist(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            email = userform.cleaned_data['email']

            User.objects.create(username=username, password=password, email=email)
            
            
            return render_to_response('regist_success.html')
            
    else:
        userform = UserForm()
    return render_to_response('regist.html', {'userform':userform})




def login(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']

            user = User.objects.filter(username__exact=username,password__exact=password)

            if user:
                return render_to_response('index.html', {'userform':userform})
            else:
                return HttpResponse('用户名或密码错误,请重新登录')

    else:
        userform = UserForm()
    return render_to_response('login.html', {'userform':userform})
	

  

@login_required
def index(req):
    username = req.COOKIES.get('username', '')
    return render_to_response('index.html', {'username':username})


def logout(req):
    response = render_to_response('log_out.html')
    response.delete_cookie('username')
    return response

