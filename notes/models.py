from django.db import models

# Create your models here.
class Note(models.Model):
  title = models.CharField(max_length=100, default =""
  )
  description = models.TextField(
    help_text="Enter note information", default="")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str_(self):
    return self.title

# class Note(models.Model):
#   body = models.CharField(max_length=255)
#   note = models.ForeignKey(to=Notes, on_delete=models.CASCADE, related_name='body')
#   created_at = models.DateTimeField(auto_now_add=True)
#   updated_at = models.DateTimeField(auto_now=True)

#   def __str_(self):
#     return self.body