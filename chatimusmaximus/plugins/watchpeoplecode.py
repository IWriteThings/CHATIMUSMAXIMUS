from plugins import IPlugin
from utils import Messager
from communication_protocols import ReadOnlyWebSocket

class WatchPeopleCodePlugin(IPlugin):
    def __init__(self, settings): 
        # use the trivial instance `_messager` to get around multiple inheritance
        # problems with PyQt
        self._messager = Messager('watchpeoplecode')
        # Duck type the `chat_signal` onto the `Socket` instance/class
        self.chat_signal = self._messager.chat_signal
        streamer_name = settings['channel']
        self._websocket = ReadOnlyWebSocket(streamer_name,
                                            '/chat',
                                            'http://www.watchpeoplecode.com/socket.io/1/',
                                            self._messager.recieve_chat_data)
        


