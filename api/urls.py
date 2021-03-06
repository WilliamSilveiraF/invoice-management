from django.urls import path
from . import views
from rest_framework_simplejwt.views import (TokenRefreshView)

urlpatterns = [
    path('invoice/', views.InvoiceView.as_view(), name='Invoice'),

    path('auth/', views.GetRoutesView.as_view(), name='get_routes'),
    path('auth/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register', views.NewUserView.as_view(), name='register')
]