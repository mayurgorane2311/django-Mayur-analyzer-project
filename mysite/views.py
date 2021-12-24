# mayur gorane are interesting men and is required absolute solution
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     m = "<h1>mayur gorane personal nevigator<h1> <a href=https://www.w3schools.com>Visit W3Schools.com!</a> <br> "
#     return HttpResponse(m)
def index(request):
    return render(request,'index.html')

def about(request):
    djtext = (request.POST.get('text', 'default'))
    about = (request.POST.get('about', 'off'))
    upper = (request.POST.get('Upper', 'off'))
    newline = (request.POST.get('newline', 'off'))
    extraspace = (request.POST.get('extraspace', 'off'))
    counter = (request.POST.get('counter', 'off'))
    print(djtext)
    print(about)
    if about == "on":
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'with Removed Punctuation', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'about.html', params)

    if (upper == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'automatically uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'about.html', params)

    if (extraspace == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not (djtext[index] ==  " " and djtext[index +1] == "  "):
                analyzed = analyzed + char

        params = {'purpose': 'extra space remove', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'about.html', params)

    if (counter == "on"):
        analyzed = len(djtext)
        params = {'purpose': 'count your word ', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'about.html', params)


    if (newline == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'no space in line', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'about.html', params)

    if (about != "on" and upper != "on" and extraspace != "on" and counter != "on" and newline != "on")     :
        return HttpResponse("error")

    return render(request, 'about.html', params)

def new(request):
    return HttpResponse('this new line')



# def ex1(request):
#     s=''' <h1> Navigation Bar </h2> <br>
#     <a href= "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9" > Django Code With Harry Bhai </a><br>
#     <a href="https://www.facebook.com/"> Facebook </a> <br>
#     <a href="https://www.flipkart.com/"> Flipkart </a> <br>
#     <a href="https://www.hindustantimes.com/"> News </a> <br>
#     <a href="https://www.google.com/"> Google </a> <br>'''
#     return HttpResponse(s)

