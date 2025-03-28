from django.shortcuts import render
from django.http import HttpResponse
"""   
Mantıksal işlemleri veri işleme süreçlerini yönetir
http isteği alır ve http yanıtı döndürür
frontend ile backend arasında köprü görevi görür

"""
def index (request):
    return HttpResponse("you are at the polls index")

def index2 (request):
    return HttpResponse("you are at the polls index2")
