from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.UserListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^~enter/$',
        view=views.enter_view,
        name='enter'
    ),
    url(
        regex=r'^~redirect/$',
        view=views.UserRedirectView.as_view(),
        name='redirect'
    ),
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^~update/$',
        view=views.UserUpdateView.as_view(),
        name='update'
    ),
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.StudentDetailView.as_view(),
        name='detail_student'
    ),
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.TeacherDetailView.as_view(),
        name='detail_teacher'
    ),
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.ParentDetailView.as_view(),
        name='detail_parent'
    ),
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.ManagementDetailView.as_view(),
        name='detail_management'
    ),
]
