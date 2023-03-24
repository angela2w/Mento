from django.shortcuts import render

def Home(request):
    return render(request,'index.html')
def About(request):
    return render(request, 'about.html')
def contact(request):
    return  render(request,'contact.html')
def Details (request):
    return render(request, 'course-details.html' )
def Course (request):
    return render(request,'courses.html')
def Events(request):
    return render(request,'events.html')
def Pricing(request):
    return render(request,'pricing.html')
def Trainers(request):
    return render(request,'trainers.html')