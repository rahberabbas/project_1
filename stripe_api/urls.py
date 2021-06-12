from django.urls import path
from stripe_api import views

urlpatterns = [
    path('test-payment/', views.test_payment),
    path('save-stripe-info/', views.save_stripe_info),
    path('confirm-payment-intent/', views.confirm_payment_intent)
]
