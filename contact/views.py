from contextlib import ContextDecorator

from django.shortcuts import redirect, render

from .forms import ContactForm


# Create your views here.
def contact_form(request):
    msg = ''
    if request.method == 'POST':
        form1 = ContactForm(request.POST)

        if form1.is_valid():
            msg = 'Success!'
        else:
            msg = 'Fail!'

    else:
        form1 = ContactForm()

    return render(request, 'contact_form.html', {'form': form1, 'msg': msg})
