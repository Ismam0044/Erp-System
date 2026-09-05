from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import include, path

from core.views import dashboard


def trigger_error(request):
    # Temporary: verifies Sentry is receiving events. Remove after confirming.
    1 / 0


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
    path("inventory/", include("inventory.urls")),
    path("sentry-debug/", login_required(trigger_error)),
]
