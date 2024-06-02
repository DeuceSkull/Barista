from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView


class ProductList(ListView):
    model = Product
    extra_context = {
        'title': 'Totembo: Main page'
    }
    template_name = 'store/product_list.html'


def reservation(request):
    return render(request, 'store/reservation.html')
