from django import forms

class ScreenForm(forms.Form):
    name = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
from django.shortcuts import render
from .forms import ScreenForm

def screen_view(request):
    form = ScreenForm()
    return render(request, 'screen.html', {'form': form})
<form action="{% url 'screen' %}" method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Submit">
</form>
