from django.shortcuts import render
from django.http import HttpResponse


def page1(request):
    return HttpResponse("<body style='background-color: black; color: yellow'><h1><b>PAGE 1</b></h1><br><a href='http://127.0.0.1:8000/page5'><button>Previous page</button></a> <a href='http://127.0.0.1:8000/page2/'><button>Next page</button></a></body>")
def page2(request):
    return HttpResponse("<body style='background-color: black; color: yellow'><h1><b>PAGE 2</b></h1><br><a href='http://127.0.0.1:8000'><button>Previous page</button></a> <a href='http://127.0.0.1:8000/page3/'><button>Next page</button></a></body>")
def page3(request):
    return HttpResponse("<body style='background-color: black; color: yellow'><h1><b>PAGE 3</b></h1><br><a href='http://127.0.0.1:8000/page2/'><button>Previous page</button></a> <a href='http://127.0.0.1:8000/page4/'><button>Next page</button></a></body>")
def page4(request):
    return HttpResponse("<body style='background-color: black; color: yellow'><h1><b>PAGE 4</b></h1><br><a href='http://127.0.0.1:8000/page3/'><button>Previous page</button></a> <a href='http://127.0.0.1:8000/page5/'><button>Next page</button></a></body>")
def page5(request):
    return HttpResponse("<body style='background-color: black; color: yellow'><h1><b>PAGE 5</b></h1><br><a href='http://127.0.0.1:8000/page4/'><button>Previous page</button></a> <a href='http://127.0.0.1:8000'><button>Next page</button></a></body>")
