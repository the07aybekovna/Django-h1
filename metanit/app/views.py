from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Main Page</h1>")

def products(request):
    return HttpResponse("<h1>Products</h1>"
                        "<ul>"
                        "<li>Phone</li>"
                        "<li>Laptop</li>"
                        "<li>iPad</li>"
                        "</ul>")
def users(request):
    return HttpResponse("<h1>Users</h1>"
                        "<ol>"
                        "<li>Mia Yilin</li>"
                        "<li>Yu Xua</li>"
                        "<li>George Orwel</li>"
                        "</ol>")