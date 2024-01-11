from django.shortcuts import render
from .models import music

def wap(request):
    pop=music.objects.filter(name='guc')
    pop1=music.objects.filter(name='asake')
    return render(request,'index.html',{"pop":pop,"pop1":pop1})