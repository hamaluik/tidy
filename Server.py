import sys
import cherrypy
from cherrypy.lib import auth_digest
import hashlib
import os
import markdown

class Server(object):
	def __init__(self):
		super(Server, self).__init__()

	@cherrypy.expose
	def default(self, *args, **kwargs):
		# open the template file
		with open('static/index.html', 'r') as templateFile:
			html = templateFile.read()

		# and return the templated file
		return html

if __name__ == '__main__':
	# setup the cherrypy configuration
	cherrypy.server.socket_host = '0.0.0.0'
	cherrypy.server.socket_port = 5000
	conf = {
		'/': {
			'tools.staticdir.root': os.path.abspath(os.getcwd()),
		},
		'/css': {
			'tools.staticdir.on': True,
			'tools.staticdir.dir': os.path.join('static', 'css')
		},
		'/js': {
			'tools.staticdir.on': True,
			'tools.staticdir.dir': os.path.join('static', 'js')
		},
		'/fonts': {
			'tools.staticdir.on': True,
			'tools.staticdir.dir': os.path.join('static', 'fonts')
		},
		'/img': {
			'tools.staticdir.on': True,
			'tools.staticdir.dir': os.path.join('static', 'img')
		},
	}

	# disable auto-reload
	cherrypy.config.update({'engine.autoreload.on': False})

	# initialize the server
	app = Server()

	# start the server
	cherrypy.quickstart(app, '/', conf)