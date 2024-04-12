
from django.http import HttpResponse
from django.shortcuts import render

def home(request):

    return render(request,'home.html')


def post(request):
  
    text=(request.POST.get('text','default'))
    punc=(request.POST.get('remove','off'))
    uper=(request.POST.get('uppercase','off'))
    newl=(request.POST.get('newline','off'))
    space=(request.POST.get('spaceremover','off'))
    countchar=(request.POST.get('countchar','off'))
    
    if punc=='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=''
        
        for char in text:
            if char  not in punctuations:
                analyzed+=char
        params={"purpose":"remove punc","ananly_text":analyzed}
        text=analyzed
        
    if(uper=="on"):
        analyzed=''
        for char in text:
         analyzed+=char.upper()
        params={"purpose":"uppercase","ananly_text":analyzed}
       
        text=analyzed
        
    if(newl=="on"):
        analyzed=''
        for char in text:
         if char!=("\n") and char!='\r':
          analyzed+=char
        params={"purpose":"remove new line","ananly_text":analyzed}
       
        text=analyzed
    if(space=="on"):
        analyzed=''
        for index,char in enumerate(text):
             if not(text[index] == " " and text[index+1]==" "):
                analyzed = analyzed + char
        params={"purpose":"space ","ananly_text":analyzed}
       
        text=analyzed
    
    if(countchar=="on"):
        charcount=(len(text))
        analyzed=charcount
        params={"purpose":"count","ananly_text":analyzed}
     
        text=analyzed
    if(punc!="on" and newl!="on" and space!="on" and uper!="on"):
          return HttpResponse("please select any operation and try again")
    
    return render(request,"post.html",params)
   
