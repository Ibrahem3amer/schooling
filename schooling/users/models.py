from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    USER_TYPE = (
        ('STD', 'student'),
        ('MNG', 'management'),
        ('PRT', 'parent'),
        ('TCH', 'teacher'),
    )
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    user_type = models.CharField(max_length=3, choices=USER_TYPE)

    def __str__(self):
        return self.username


class School(models.Model):
    """
    A model that represents the school entity.
    """
    name = models.CharField(max_length=220)
    address = models.CharField(max_length=220)
    phone = models.CharField(max_length=220)
    headmaster = models.CharField(max_length=220)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Management(User):
    """
    A model that represents the school management membership.
    """
    name_in_admin = models.CharField(max_length=10, default='management')
    school = models.OneToOneField(
        to=School,
        related_name='management',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail_management', kwargs={'username': self.username})


@python_2_unicode_compatible
class Teacher(User):
    """
    A model that represents the teacher membership.
    """
    name_in_admin = models.CharField(max_length=10, default='teacher')
    school = models.ForeignKey(
        to=School,
        related_name='teacher',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail_teacher', kwargs={'username': self.username})


@python_2_unicode_compatible
class Student(User):
    """
    A model that represetns the student membership.
    """
    name_in_admin = models.CharField(max_length=10, default='student')
    school = models.ForeignKey(
        to=School,
        related_name='Student',
        on_delete=models.CASCADE,
     )

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail_student', kwargs={'username': self.username})


@python_2_unicode_compatible
class Parent(User):
    """
    A model that represents the parent membership
    """
    name_in_admin = models.CharField(max_length=10, default='parent')
    son = models.ForeignKey(
        to=Student,
        related_name='Parent',
        on_delete=models.CASCADE,
     )

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail_parent', kwargs={'username': self.username})
