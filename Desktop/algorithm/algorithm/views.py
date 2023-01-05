from django.shortcuts import render, redirect
from ..ChrysalisWebApp.forms import ScreenForm

def screen_view(request):
    if request.method == 'GET':
        form = ScreenForm()
        return render(request, 'screen.html', {'form': form})
    elif request.method == 'POST':
        form = ScreenForm(request.POST)
        if form.is_valid():
            input_choice = form.cleaned_data['input_choice']
            return redirect('some_url')