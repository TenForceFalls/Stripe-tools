##Payment intent canel tool

import stripe

# Set your Stripe secret key
stripe.api_key = 'Enter your api key here'

def cancel_payment_intent(payment_intent_id):
    try:
        # Cancel the payment intent
        intent = stripe.PaymentIntent.cancel(payment_intent_id)
        print(f"Payment Intent {payment_intent_id} has been successfully canceled.")
        return intent
    except stripe.error.StripeError as e:
        print(f"Failed to cancel payment intent: {e.user_message}")
        return None

if __name__ == "__main__":
    payment_id = input("Enter the Payment Intent ID to cancel: ")
    cancel_payment_intent(payment_id)
