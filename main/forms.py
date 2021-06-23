from .models import Task
from django.forms import ModelForm, TextInput, Textarea, CheckboxInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "text", "done"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
            "done": CheckboxInput(attrs={
                'class': 'required checkbox form-control'
            }),
        }