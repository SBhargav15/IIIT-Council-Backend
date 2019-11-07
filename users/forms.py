from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User
from django import forms

class userCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model=User
        fields=('username','email','is_superuser','is_admin','is_college_staff')

    def clean_username(self):
        username=self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['Username already exits'])
class userChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model=User
        fields=('username','email')