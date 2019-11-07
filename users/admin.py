from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User
from colleges.models import Profile
from users.forms import userCreationForm,userChangeForm
# Register your models here.

class ProfileInline(admin.StackedInline):
    model=Profile
    can_delete=False
    verbose_name_plural='Profile'

class CustomUserAdmin(UserAdmin):
    form=userChangeForm
    add_form=userCreationForm

    fieldsets = UserAdmin.fieldsets + (
            (('Flags'), {'fields': ('is_admin','is_college_staff')}),
    )




    inlines=(ProfileInline,)
    list_display=('username','email','first_name','last_name','is_admin','is_college_staff','is_superuser')
    def get_inline_instances(self,request,obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin,self).get_inline_instances(request,obj)    

admin.site.register(User, CustomUserAdmin)