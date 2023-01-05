from django.shortcuts import render
from .forms import ScreenForm

def screen_view(request):
    if request.method == 'POST':
        form = ScreenForm(request.POST)
        if form.is_valid():
            # process the form data
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            # do something with the form data here
            # ...
            return redirect('some_url')
    else:
        form = ScreenForm()
    return render(request, 'screen.html', {'form': form})