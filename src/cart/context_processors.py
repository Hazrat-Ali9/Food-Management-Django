from .cart import Cart
# context processor
def cart(request):
    return {'cart': Cart(request)}