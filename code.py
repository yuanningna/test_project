from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>首页</h1>')
