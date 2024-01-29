from django.shortcuts import render,redirect
from django.http import HttpResponse
import random
from . models import *
import os
from django.conf import settings

# Create your views here.
def home(request):
    return render(request,'landing.html')

              
def themes(request):
    return render(request , 'theme_selection.html')



qlist = None
charlist = None
question = None
def chara(request):
    global qlist
    global charlist
    qlist = list(Charquestions.objects.all())
    qlist =[
        str(q) for q in qlist
    ]
    charlist = list(Chardata.objects.all())
    charlist = [  
        {
            'name':obj.name,
            'male':obj.male,
            'female':obj.female,
            'human':obj.human,
            'youtuber':obj.youtuber,
            'actor':obj.actor,
            'real':obj.real,
            'Indian':obj.Indian,
            'American':obj.American,
            'scientist':obj.scientist,
            'Singer':obj.Singer
        }
        for obj in charlist
    ]
    return redirect('playgame')



lastkeyword=None
lastanswer=None
def getlastkeyword(question):
    global lastkeyword
    k = ['male','female','human','youtuber','actor','real','Indian','American','scientist','Singer','Politician']
    for i in k:
        if i in question:
            lastkeyword=i
        

def filtercharlist(lastkeyword,lastanswer,charlist):
    to_remove=[]
    if lastanswer == 'Yes':
        lastanswer =True
    elif lastanswer == 'No':
        lastanswer = False
    else:
        return
    
    for i in charlist:
        if i[lastkeyword] != lastanswer:
            to_remove.append(i) 

    for i in to_remove:
        charlist.remove(i)


def getlastanswer(request):
    global lastanswer
    lastanswer = request.POST.get("answer")
    return lastanswer

def playgame(request):
    global qlist
    global charlist
    global question 
    global lastkeyword
    global lastanswer
    question = random.choice(qlist)
    lastanswer=getlastanswer(request)
    try:
        filtercharlist(lastkeyword,lastanswer,charlist)
    except Exception as e:
        print(e)
    getlastkeyword(question)


    qlist.remove(question)

    if len(charlist)==1:
        context ={'name':charlist[0]['name']}
        return render(request,'result.html',context)
    
    elif len(charlist) < 1:
        context={'name':'Couldnt find your character'}
        return render(request,'result.html',context)
    
    dir = settings.BASE_DIR

    print("The dir path from the settings is :",dir)
    image = os.listdir(f"{dir}/static/poses")
    image = random.choice(image)
    print(image)
    context ={'randomquestion':question,'image':image}
    return render(request,'playgame.html',context)


def obj(request):
    return HttpResponse("welcome to object game , we are still developing it")
def ani(request):
    return HttpResponse("welcome to animal game , we are still developing it.")
