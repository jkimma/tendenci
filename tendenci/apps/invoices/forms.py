from django import forms

from tendenci.apps.invoices.models import Invoice

class AdminNotesForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('admin_notes',
                  )
        
        
class AdminAdjustForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('variance',
                  'variance_notes',
                  )
