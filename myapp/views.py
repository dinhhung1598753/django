from django.shortcuts import render
from django.views import View
from .models import NhaSanXuat, MatHang
# Create your views here.

class NSX(View):

    def get(self, request):
        nst = NhaSanXuat.objects.all()
        sp = MatHang.objects.all()
        text = {
            'h':nst,
            'h1': sp
        }

        return render(request, 'index.html', text)

class NSXX(View):

    def get(self, request):
        nst = NhaSanXuat.objects.all()
        sp = MatHang.objects.all()
        text = {
            'h':nst,
            'h1': sp
        }

        return render(request, 't.html', text)