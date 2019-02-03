from django.shortcuts import render


def home(request):
	return render(request,  "home.html", {})

def about(request):
	from pages.about import aboutme
	return render(request,  "about.html", {"about_me":aboutme})

def services(request):
	return render(request,  "services.html", {})
