""" Middleware Configuration Settings """
from masonite.middleware import ResponseMiddleware, SecureHeadersMiddleware, CorsMiddleware

from app.http.middleware.AddAttributeMiddleware import AddAttributeMiddleware
from app.http.middleware.AuthenticationMiddleware import AuthenticationMiddleware
from app.http.middleware.CsrfMiddleware import CsrfMiddleware
from app.http.middleware.LoadUserMiddleware import LoadUserMiddleware
from app.http.middleware.MiddlewareTest import MiddlewareTest


"""
|--------------------------------------------------------------------------
| HTTP Middleware
|--------------------------------------------------------------------------
|
| HTTP middleware is middleware that will be ran on every request. Middleware
| is only ran when a HTTP call is successful (a 200 response). This list
| should contain a simple aggregate of middleware classes.
|
"""

HTTP_MIDDLEWARE = [
    LoadUserMiddleware,
    # todo
    # CsrfMiddleware,
    CorsMiddleware,
    ResponseMiddleware,
    SecureHeadersMiddleware,
]

"""
|--------------------------------------------------------------------------
| Route Middleware
|--------------------------------------------------------------------------
|
| Route middleware is middleware that is registered with a name and can
| be used in the routes/web.py file. This middleware should really be
| used for middleware on an individual route like a dashboard route.
|
| The Route Middleware is a dictionary with the key being what is specified
| in your route/web.py file (in the .middleware() method) and the value is
| a string with the full module path of the middleware class
|
"""

ROUTE_MIDDLEWARE = {
    'auth': AuthenticationMiddleware,
    'test': MiddlewareTest,
    'cors': CorsMiddleware,
    'middleware.test': [
        MiddlewareTest,
        AddAttributeMiddleware,
    ]
}

"""Secure Headers to use in masonite.middlware.SecureHeadersMiddleware"""

SECURE_HEADERS = {
    'Strict-Transport-Security': 'max-age=63072000; includeSubdomains',
    'X-Frame-Options': 'SAMEORIGIN',
    'X-XSS-Protection': '1; mode=block',
    'X-Content-Type-Options': 'sniff-test',
    'Referrer-Policy': 'no-referrer, strict-origin-when-cross-origin',
    'Cache-control': 'no-cache, no-store, must-revalidate',
    'Pragma': 'no-cache',
}

CORS = {
    'Access-Control-Allow-Origin': "*",
    "Access-Control-Allow-Methods": "DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT",
    "Access-Control-Allow-Headers": "Content-Type, Accept, X-Requested-With",
    "Access-Control-Max-Age": "3600",
    "Access-Control-Allow-Credentials": "true"
}
