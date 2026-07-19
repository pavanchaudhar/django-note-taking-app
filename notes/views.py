from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm

def home(request):
    return render(request, "home.html")


def add_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = NoteForm()

    return render(request, "add_note.html", {"form": form})

def note_list(request):
    notes = Note.objects.all().order_by("-created_at")
    return render(request, "note_list.html", {"notes": notes})