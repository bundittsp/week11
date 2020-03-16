from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=10, label='หัวข้อ')
    message = forms.CharField(widget=forms.Textarea, label='ข้อความ')
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
    TYPES = (
        ('01', 'Business'),
        ('02', 'Casual'),
        ('03', 'Others'),
    )
    contact_type = forms.ChoiceField(choices=TYPES, required=True, initial='02')
    contact_date = forms.DateField(
        input_formats=['%Y-%m-%d', '%d/%m/%Y'], 
        help_text='Date formats: YYYY-MM-DD or DD/MM/YYYY'
    )

    cc_myself.widget.attrs.update({'class': 'form-check-input'})
    subject.widget.attrs.update({'class': 'form-control'})
    message.widget.attrs.update({'class': 'form-control'})
    sender.widget.attrs.update({'class': 'form-control', 'placeholder': 'โปรดกรอกอีเมล'})
    contact_type.widget.attrs.update({'class': 'form-control'})
    contact_date.widget.attrs.update({'class': 'form-control'})