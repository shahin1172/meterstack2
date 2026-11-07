from django.urls import path,include

from .views import DummyDetailView

urlpatterns = [
    path(
        "api/dummy/<slug:tenant_slug>/",
        DummyDetailView.as_view(),
        name="dummy-detail",


    ),
    path("api/v1/", include("users.urls")),
]