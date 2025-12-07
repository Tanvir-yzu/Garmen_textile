from django.shortcuts import render
from datetime import datetime

def home(request):
    return render(request, "home.html", {"current_year": datetime.now().year})
