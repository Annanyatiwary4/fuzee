import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from room import routing  # Import your app's routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fuze.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns  # Define your WebSocket URLs
        )
    ),
})