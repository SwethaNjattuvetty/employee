from django.shortcuts import render,redirect
from app1.models import Employee
# Create your views here.

def home(request):
    k = Employee.objects.all()
    return render(request,'home.html',{'employee':k})
def add(request):
    if request.method=="POST":
        n = request.POST['n']
        a = request.POST['a']
        ad = request.POST['ad']
        em = request.POST['em']
        i = request.FILES['i']

        k=Employee.objects.create(name=n,age=a,address=ad,email=em,image=i)
        k.save()
        return home(request)
    return render(request,'add.html',)

def edit(request,i):
    k=Employee.objects.get(id=i)

    if request.method=="POST":
        k.name=request.POST['n']
        k.age=request.POST['a']
        k.address = request.POST['ad']
        k.email = request.POST['em']

        if request.FILES.get('i')==None:
            k.save()
        else:
            k.image=request.FILES.get('i')
        k.save()

        return redirect('app1:home')
    return render(request, 'edit.html', {'employee': k})


def delete(request,i):

    k = Employee.objects.get(id=i)
    k.delete()
    return redirect('app1:home')

