from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from core.views import dashboard

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("", dashboard, name="dashboard"),
    path("sales/", include("sales.urls")),
    path("purchase/", include("purchase.urls")),
    path("parties/", include("parties.urls")),
    path("accounts/", include("accounts.urls")),
    path("reports/", include("reports.urls")),
]
