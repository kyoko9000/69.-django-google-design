from django.shortcuts import render


# Create your views here.
def home(request):
    print("ok")
    if request.method == "POST":
        text = request.POST['text_1']
        print("data", text)

    return render(request, "home/test.html")