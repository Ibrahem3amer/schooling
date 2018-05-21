from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Teacher, Parent, Student, School, Management


admin.site.register(Teacher)
admin.site.register(Parent)
admin.site.register(Student)
admin.site.register(School)
admin.site.register(Management)


#class MyUserChangeForm(UserChangeForm):
#    class Meta(UserChangeForm.Meta):
#        model = User


#class MyUserCreationForm(UserCreationForm):

#    error_message = UserCreationForm.error_messages.update({
#        'duplicate_username': 'This username has already been taken.'
#    })

#    class Meta(UserCreationForm.Meta):
#        model = User

#    def clean_username(self):
#        username = self.cleaned_data["username"]
#        try:
#            User.objects.get(username=username)
#        except User.DoesNotExist:
#        raise forms.ValidationError(self.error_messages['duplicate_username'])


#@admin.register(User)
#class MyUserAdmin(AuthUserAdmin):
#    form = MyUserChangeForm
#    fieldsets = (
#            ('User Profile', {'fields': ('name',)}),
#    ) + AuthUserAdmin.fieldsets
#    search_fields = ['name']
