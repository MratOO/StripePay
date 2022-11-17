import stripe
from django.shortcuts import redirect
from django.conf import settings
from django.views import View
from django.views.generic import DetailView, TemplateView

from .models import Item


stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    template_name = 'stripe_payment/success.html'


class CancelView(TemplateView):
    template_name = 'stripe_payment/cancel.html'
    

class ItemDetailView(DetailView):
    model = Item
    template_name = 'stripe_payment/index.html'
    context_object_name = 'item_detail'


class CreateCheckoutSessionView(View):
    def get(self, request, *args, **kwargs):
        item_id = self.kwargs['pk']
        item = Item.objects.get(id=item_id)
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': item.price,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://localhost:8000/success',
            cancel_url='http://localhost:8000/cancel',
        )

        return redirect(session.url, code=303)
