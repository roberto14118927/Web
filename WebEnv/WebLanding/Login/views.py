from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth import authenticate

from django.contrib.auth import login as login_django


class LoginClass(View):
    templates = 'Login/Login.html'
    templates_ok = 'Landing/Landing.html'
    def get(self, request, *args, **kwargs):
        #print("SOY GET")
        if request.user.is_authenticated:
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('Dashboard:Dashboard')
        return render(request, self.templates,{})


    def post (self, request, *args, **kwargs):
        user_post = request.POST['user']
        password_post = request.POST['password']
        #ACÁ TRAIGO LO QUE TENGO EN LA VISTA
        user_session = authenticate(username = user_post, password = password_post)
        #ACÁ LO VALIDO 
        if user_session is not None:
            login_django(
                request, user_session
            )
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('Dashboard:Dashboard')
        else: 
            self.message = 'Usuario o contraseña incorrecto'
        
        return render(request, self.templates, self.get_context())

    def get_context(self):
        return{
           'error': self.message
        }


