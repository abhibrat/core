# import app
# from config import database
from wsgi import container
import asyncio
import time
import inspect

async def main(providers):
    for provider in container.make('WSGIProviders'):
        # print(provider)
        # container.resolve(provider.boot)
        if inspect.iscoroutinefunction(provider.boot):
            await container.resolve(provider.boot)
        else:
            container.resolve(provider.boot)


class Asgi():
    def __init__(self, scope):
        self.scope = scope

    async def __call__(self, receive, send):

        """Add Environ To Service Container
        Add the environ to the service container. The environ is generated by the
        the WSGI server above and used by a service provider to manipulate the
        incoming requests
        """

        container.bind('Environ', self.scope)

        """Execute All Service Providers That Require The WSGI Server
        Run all service provider boot methods if the wsgi attribute is true.
        """

        try:
            await main(container.make('WSGIProviders'))
                
        except Exception as e:
            container.make('ExceptionHandler').load_exception(e)

        """We Are Ready For Launch
        If we have a solid response and not redirecting then we need to return
        a 200 status code along with the data. If we don't, then we'll have
        to return a 302 redirection to where ever the user would like go
        to next.
        """

        # start_response(container.make('Request').get_status_code(),
        #             container.make('Request').get_and_reset_headers())

        """Final Step
        This will take the data variable from the Service Container and return
        it to the WSGI server.
        """

        # return iter([bytes(container.make('Response'), 'utf-8')])
        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers': [
                [b'content-type', b'text/html'],
            ],
        })
        await send({
            'type': 'http.response.body',
            'body': bytes(container.make('Response'), 'utf-8'),
        })
