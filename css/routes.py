from flask import render_template, request
from app import app
import stripe

stripe.api_key = app.config['sk_test_51NHeAeBy2dVhOoaCHLphc6twhC1j9tfklBOBo5FeVA6xJXjmaVMQHc6jjpaSlAAHARHXIugseYTaobgh1Ey4daOK00Bkfp5LPe']

@app.route('/payment_complete')
def payment_complete():
    return render_template('payment_complete.html')

@app.route('/pay', methods=['POST'])
def pay():
    winner_email = request.form['email']  

    payment_amount = 10

    payment_intent = stripe.PaymentIntent.create(
        amount=payment_amount,
        currency='usd',
        payment_method_types=['card'],
        receipt_email=winner_email,
        description='Game payment'
    )

    return {
        'clientSecret': payment_intent.client_secret
    }

