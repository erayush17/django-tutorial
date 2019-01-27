from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    
    my_context = {
        "my_text": "This is home view context.",
        "my_number": 123,
        "my_list": [123, 7843, 9090, 21312]
    }
    return render(request, "home.html", my_context) # home.html template