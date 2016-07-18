import falcon
import json
import core
from wsgiref import simple_server

class SmartChainAPI(object):
    def on_get(self, req, resp):
        """ On GET Request """

        server_core = core.core()
        url = req.get_param('url')

        content = server_core.process_data(url)

        resp.status = falcon.HTTP_200
        resp.body = json.dumps(content)

if __name__ == '__main__':
	# Starts Falcon API
	api = application = falcon.API()

	# Add routes
	# URL Pattern: /api?url=URL_PATH
	api.add_route('/api', SmartChainAPI())

	# Host api using wsgiref simple_server
	httpd = simple_server.make_server('127.0.0.1', 8000, api)
	httpd.serve_forever()