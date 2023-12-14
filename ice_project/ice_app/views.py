from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import iceform
from .models import icecream


# Create your views here.
def index(request):
    # return HttpResponse("hhhhh")
    ice = icecream.objects.all()
    context = {  # its optional
        'icecream_list': ice
    }

    return render(request,"index.html",context)

# def detail(request,ice_id):
#     return HttpResponse("this is movie is %s" % ice_id)  #%s using print string

# fech datas in db
def detail(request,ice_id):
    f=icecream.objects.get(id=ice_id)
    return render(request,"detail.html",{'ice':f})

# img=img

def add_icecream(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc = request.POST.get('desc', )
        price = request.POST.get('price', )
        img = request.FILES['img']
        ice3=icecream(name=name,desc=desc,price=price,img=img)
        ice3.save()
    return render (request,"add.html")

def update(request,id):
    ic=icecream.objects.get(id=id)
    ice5=iceform(request.POST or None,request.FILES,instance=ic)
    if ice5.is_valid():
        ice5.save()
        return redirect('/')
    return render(request,'edit.html',{'form':ice5,'tbl':ic})

def delete(request,id):
    if request.method=='POST':
        dlt=icecream.objects.get(id=id)
        dlt.delete()
        return redirect('/')
    return render(request,'delete.html')