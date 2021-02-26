'''qfieldcloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path(
        '', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path(
        '', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path(
        'blog/', include('blog.urls'))
'''
from django.contrib import admin
from django.urls import path, re_path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from qfieldcloud.core.views import auth_views

from qfieldcloud.web.views import (
    projects_views,
    organizations_views,
    settings_views,
    pages_views
)

schema_view = get_schema_view(
    openapi.Info(
        title='QFieldcloud REST API',
        default_version='v1',
        description='Test description',
        terms_of_service='https://',
        contact=openapi.Contact(email='info@opengis.ch'),
        license=openapi.License(name='License'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path(
        'docs/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),

    path('admin/', admin.site.urls),
    path('api/v1/auth/registration/', include('rest_auth.registration.urls')),
    path('api/v1/auth/token/', auth_views.AuthTokenView.as_view()),
    path('api/v1/auth/', include('rest_auth.urls')),

    path('api/v1/', include('qfieldcloud.core.urls')),
    path('auth/', include('rest_framework.urls')),

    path('accounts/', include('allauth.urls')),
    re_path(
        r'^invitations/',
        include('invitations.urls', namespace='invitations')
    ),

    path('', pages_views.index, name='index'),
    path(
        '<str:unpermitted_action>/unpermitted',
        pages_views.unpermitted,
        name='unpermitted'
    ),

    path(
        'settings/<str:username>/',
        settings_views.SettingsUserView.as_view(),
        name='settings_user'
    ),
    path(
        'settings/<str:username>/profile',
        settings_views.SettingsProfileView.as_view(),
        name='settings_profile'
    ),
    path(
        'settings/<str:username>/databases',
        settings_views.SettingsDatabasesView.as_view(),
        name='settings_databases'
    ),
    path(
        'settings/<str:username>/security',
        settings_views.SettingsSecurityView.as_view(),
        name='settings_security'
    ),
    path(
        'settings/<str:username>/organizations',
        settings_views.SettingsOrganizationsView.as_view(),
        name='settings_organizations'
    ),
    path(
        'settings/<str:username>/members',
        settings_views.SettingsMembersView.as_view(),
        name='settings_members'
    ),

    path(
        'projects/create/',
        projects_views.ProjectCreateView.as_view(),
        name='project_create'
    ),

    path(
        'organizations/create/',
        organizations_views.OrganizationCreateView.as_view(),
        name='organization_create'
    ),

    path(
        '<str:username>/',
        projects_views.ProjectFilterListView.as_view(),
        name='profile_overview'
    ),
    path(
        '<str:username>/<str:project>/',
        projects_views.ProjectOverviewView.as_view(),
        name='project_overview'
    ),
    path(
        '<str:username>/<str:project>/files',
        projects_views.ProjectFilesView.as_view(),
        name='project_files'
    ),
    path(
        '<str:username>/<str:project>/changes',
        projects_views.ProjectChangesListView.as_view(),
        name='project_changes'
    ),
    path(
        '<str:username>/<str:project>/collaborators',
        projects_views.ProjectCollaboratorsView.as_view(),
        name='project_collaborators'
    ),
    path(
        '<str:username>/<str:project>/collaborators/invite',
        projects_views.ProjectCollaboratorsInviteView.as_view(),
        name='project_collaborators_invite'
    ),
    path(
        '<str:username>/<str:project>/yolo',
        projects_views.ProjectYoloView.as_view(),
        name='project_yolo'
    ),
]
