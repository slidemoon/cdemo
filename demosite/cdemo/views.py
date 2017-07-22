from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Project, Content


# Create your views here.

def login(request):
    if request.GET.get('next'):
        content = {'next': request.GET['next']}
        return render(request, 'cdemo/login.html', content)
    else:
        return render(request, 'cdemo/login.html')

def login_result(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        auth_login(request, user)
        full_path = request.get_full_path()
        if 'next' in full_path:
            next_url = full_path.split('=')[1]
            return HttpResponseRedirect(next_url)
        else:
            return HttpResponseRedirect(reverse('cdemo:main'))
    else:
        return HttpResponse('fail to login')

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('cdemo:login'))

@login_required(login_url='/cdemo/')
def main(request):
    return render(request, 'cdemo/main.html')

@login_required(login_url='/cdemo/')
def cproject(request):
    project_object_all = Project.objects.all()
    content = {'project_object_all': project_object_all}
    return render(request, 'cdemo/project.html', content)

@login_required(login_url='/cdemo/')
def ccreate_project(request):
    new_project_name  = request.POST['newprojectname']
    create_project, created = Project.objects.get_or_create(project_name = new_project_name)
    return HttpResponseRedirect(reverse('cdemo:cproject'))

@login_required(login_url='/cdemo/')
def cconfig_test(request):
    c1 = Content.objects.get(id = 6)
    context = {'context': c1}
    return render(request, 'cdemo/configtest.html', context)

@login_required(login_url='/cdemo/')
def test_cconfig_content_add(request):
    json_str = request.POST['config_content']   
    p1 = Project.objects.get(project_name = 'shenyi')
    c1 = Content(project = p1, config_text = json_str)
    c1.save()
    return HttpResponseRedirect(reverse('cdemo:cconfig_test'))




