from django.shortcuts import render
from .models import Project, Technology

# Create your views here.


def home(request):
    projects = Project.objects.all()
    technologies = Technology.objects.all()

    return render(
        request,
        "home.html",
        {
            "projects": projects,
            "technologies": technologies,
        },
    )
