from django.shortcuts import render
from .models import Product , Contact, Order, OrderUpdate
from django.http import HttpResponse
from math import ceil
import json


def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nslides = n//4 + ceil((n/4)-(n//4))

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nslides), nslides])

    # param = {'no_of_slides':nslides,'range':range(1,nslides),'product':products}
    # allProds = [[products, range(1, nslides), nslides],
    #             [products, range(1, nslides), nslides]]
    param = {'allProds':allProds}
    return render(request, 'shop/index.html', param)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method=="POST":
        name=request.POST.get('name',' ')
        email=request.POST.get('email',' ')
        phone=request.POST.get('phone',' ')
        desc=request.POST.get('desc',' ')
        print(name,email,phone,desc)
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        thank = True
        return render(request,'shop/contact.html',{'thank':thank })
    return render(request,'shop/contact.html')


def tracker(request):
    if request.method=="POST":
        orderid=request.POST.get('orderid',' ')
        email=request.POST.get('email',' ')
        try:
            order = Order.objects.filter(order_id=orderid, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderid)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str)
                    # response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/search.html')


def product(request, myid):
    # feth the product using the id
    product = Product.objects.filter(id = myid)
    return render(request, 'shop/productView.html',{'product':product[0]})


def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsjson',' ')
        name=request.POST.get('name',' ')
        email=request.POST.get('email',' ')
        address=request.POST.get('address1',' ') + " " + request.POST.get('address2',' ')
        city=request.POST.get('city',' ')
        state=request.POST.get('state',' ')
        zip_code=request.POST.get('zip_code',' ')
        phone=request.POST.get('phone',' ')
        order=Order(items_json=items_json, name=name, email=email, address=address, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank =True
        id = order.order_id
        return render(request,'shop/checkout.html', {'thank':thank, 'id':id})
    return render(request,'shop/checkout.html')
