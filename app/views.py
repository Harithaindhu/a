from atexit import register
from http.client import HTTPResponse
from turtle import position
from unicodedata import category
from django.shortcuts import render,redirect
from . models import *
from django.db.models import Q
def home(request):
    return render(request,'home.html')

def index(request):
    msgs=msg.objects.all()
    item=items.objects.all()
    return render(request,'index.html',{'item':item,'msgs':msgs})

def staff_login(request):
    if(request.method=="POST"):
        name=request.POST.get('name')
        password=request.POST.get('password')
        log_det=register.objects.get(name=name,password=password)
        print(log_det)
        return redirect('customer_det')
    else:
        return render(request,'login.html')
def review(request):
    name=request.POST['sender']
    img=request.FILES['sender_img']
    mes=request.POST['msg1']
    job=request.POST['job']
    det=msg(name=name,img=img,msg1=mes,job=job)
    det.save()
    return redirect('contact')
def staff_register(request):
    if(request.method=='POST'):
        position=request.POST.get('position')
        staff_name=request.POST.get('staff_name')
        restaurant=request.POST.get('restaurant')
        address=request.POST.get('address')
        phone_no=request.POST.get('phone_no')
        password=request.POST.get('password')
        print(position)
        if(position=="staff"):
            user=register(name=staff_name,restaurant=restaurant,position=position,address=address,phone_no=phone_no,password=password)
            user.save()
            return render(request,'login.html')
        else:
            user=register(name=staff_name,restaurant="--------------",position=position,address=address,phone_no=phone_no,password=password)
            user.save()
            return render(request,'login.html')
    else:
        return render(request,'register.html')
def main(request):
    return render(request,'home.html')
def add_restaurant(request):
    if(request.method=='POST'):
        res_name=request.POST.get('res_name')
        loc=request.POST.get('loc')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        res=restaurant(name=res_name,location=loc,address=address,ph_no=phone,email=email)
        res.save()
        return render(request,'add_restaurant.html')
    return render(request,'add_restaurant.html')
def search(request):
    restaurant=request.POST.get('restaurant')
    location=request.POST.get('location')
    print(restaurant)
    print(location)
    request.session['session4']=restaurant
    request.session['session5']=location
    return render(request,'menu.html')
def search_restaurant(request):
    restaurant=request.POST.get("restaurant")
    return render(request,'home.html')
def search_food(request):
    food=request.POST.get('search')
    print(food)
    request.session['session']=food
    return redirect(food_menu)

def customer(request):
    item=request.POST.get('nam')
    det=items.objects.get(name=item)
    request.session['session1']=item
    return render(request,'customer.html',{'det':det})
def customer_save(request):
    item=request.session['session1']
    det=items.objects.get(name=item)
    item_name=det.name
    price=det.price
    name=request.POST.get('name')
    quantity=request.POST.get('quantity')
    phone_no=request.POST.get('phno')
    address=request.POST.get('address')
    request.session['session2']=name
    request.session['session3']=address
    details=customer_details(name=name,address=address,phone_no=phone_no,item=item_name,quantity=quantity,price=price)
    details.save()   
    return redirect('customer_view')
def customer_det(request):
    det=customer_details.objects.all()
    for i in det:
        price=((i.price)*(i.quantity))
        print(price)
    return render(request,'customer_details.html',{'det':det})
def about(request):
    return render(request,'about.html')
def customer_view(request):
    name=request.session['session2']
    address=request.session['session3']
    det=customer_details.objects.filter(name=name,address=address)
    return render(request,'customer_view.html',{'det':det})
def self_del(request):
    u_id=request.POST.get('del')
    data=customer_details.objects.filter(id=u_id)
    data.delete()
    return redirect('customer_view') 
def contact(request):
    return render(request,'contact.html')

def add_item(request):
    if request.method=='POST':
        category=request.POST['category']
        name=request.POST['name']
        img=request.FILES['image']
        price=request.POST['price']
        res=request.POST['restaurant']
        print(res)
        item=items(category=category,name=name,restaurant=res,image=img,price=price)
        item.save()
        return redirect('menu')
    return render(request,'add_item.html')

def menu(request):
    re=request.POST.get('restaurant')
    location=request.POST.get('location')
    res=request.session['session4']
    loc=request.session['session5']
    print(res)
    print(location)
    if(location==None):
        print("s")
        item=items.objects.filter(restaurant=re)
        return render(request,'menu.html',{'item':item})
    else:
        rest=restaurant.objects.get(location=location,name=re)
        item=items.objects.filter(restaurant=rest.name)
        return render(request,'menu.html',{'item':item,'res':re})
def food_menu(request):
    food=request.session['session']
    print(food)
    item=items.objects.filter(name=food)
    return render(request,'food_menu.html',{'item':item})
def meals(request):
    re=request.POST.get('restaurant')
    res=request.session['session4']
    print(res)
    meals=items.objects.filter(category='meals',restaurant=res)  
    return render(request,'menu.html',{'item':meals,'res':res})
def chicken(request):
    re=request.POST.get('restaurant')
    res=request.session['session4']
    print(res)
    chicken=items.objects.filter(category='chicken items',restaurant=res)  
    return render(request,'menu.html',{'item':chicken,'res':res})
def juice(request):
    re=request.POST.get('restaurant')
    res=request.session['session4']
    print(res)
    juice=items.objects.filter(category='juice & desserts',restaurant=res)  
    return render(request,'menu.html',{'item':juice,'res':res})

def delete(request):
    u_id=request.POST.get('del')
    data=customer_details.objects.filter(id=u_id)
    data.delete()
    return redirect('customer_det') 
