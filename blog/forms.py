from django import forms

from .models import Comment

class CommenForm(forms.ModelsForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
