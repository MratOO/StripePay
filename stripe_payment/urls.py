from django.urls import path

from .views import *

urlpatterns = [
    path('buy/<int:pk>/', CreateCheckoutSessionView.as_view(), name='buy'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path('success', SuccessView.as_view(), name='success'),
    path('cancel', CancelView.as_view(), name='cancel'),
]