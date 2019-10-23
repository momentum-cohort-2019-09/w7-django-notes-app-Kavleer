from django.shortcuts import render
from notes.models import Notes

# Create your views here.
def notes_list(request):
  notes= Notes.objects.all()
  return render(request, "notes/notes_list.html", {"notes": Notes,})

def note_detail(request, id):
  note = Notes.objects.get(pk=pk)
  return render(request, "notes/note_detail.html", {"note": note})