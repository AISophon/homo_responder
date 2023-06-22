from mcdreforged.api.all import *

PLUGIN_METADATA = {
    'id': 'homo_responder',
    'version': '1.0.0',
    'name': 'HomoResponder',
    'author': 'AISophon',
    'link': 'https://github.com/AISophon/homo_responder'
}

def on_load(server: ServerInterface, old_module):
    server.logger.info('114514 plugin loaded!')

def on_unload(server: ServerInterface):
    server.logger.info('114514 plugin unloaded!')

def on_info(server: ServerInterface, info: Info):
    if info.is_player and info.content == '114514':
        server.say('[Server] 1919810')
