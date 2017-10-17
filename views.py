# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "amadonApp/index.html")

def buy(request):
    products = {
        "1":19.99,
        "2":29.99,
        "3":4.99,
        "4":49.99
    }
    if not products.get(request.POST["product"]):
        return redirect("/amadon/")
    request.session.setdefault("charge", 0)
    request.session.setdefault("number", 0)
    request.session.setdefault("total", 0)
    request.session["charge"] = products[request.POST["product"]] * int(request.POST["number"])
    request.session["number"] += int(request.POST["number"])
    request.session["total"] += products[request.POST["product"]] * int(request.POST["number"])
    return redirect("/amadon/checkout/")

def checkout(request):
    context = {
        "charge":request.session["charge"],
        "number":request.session["number"],
        "total":request.session["total"]
    }
    return render(request, "amadonApp/checkout.html", context)