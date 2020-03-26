from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth import authenticate

# Create your views here.
def LoginView(request):
    return render(request, 'Login.html',{})

def LandingView(request):
    return render(request, 'Landing.html',{})


class LoginClass(View):
    templates = 'Login/Login.html'
    templates_ok = 'Landing/Landing.html'
    def get(self, request, *args, **kwargs):
        #print("SOY GET")
        return render(request, self.templates,{})
    def post (self, request, *args, **kwargs):
        user_post = request.POST['user']
        password_post = request.POST['password']
        #ACÁ TRAIGO LO QUE TENGO EN LA VISTA
        user_session = authenticate(username = user_post, password = password_post)
        #ACÁ LO VALIDO 
        if user_session is not None:
            #return redirect('Login:Dashboard')
            return redirect('Login:Dashboard')
        else:
            self.message = 'Usuario o contraseña incorrecto'
        
        return render(request, self.templates, self.get_context())

    def get_context(self):
        return{
           'error': self.message
        }

class LandingClass(View):
    templates_ok = 'Landing/Landing.html'
    def get(self, request, *args, **kwargs):
        return render(request,self.templates_ok,{})

class DashboardClass(View):
    templates_okidoki = 'Dashboard/Dashboard.html'
    def get (self,request,*args,**kwargs):
        #printn("GET DE DASHBOARD")
        return render(request,self.templates_okidoki,{})