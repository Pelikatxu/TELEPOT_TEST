# -*- coding: utf-8 -*-

import sys
import asyncio
import telepot
import logging
from telepot.aio.delegate import per_chat_id, create_open

TOKEN = '255249816:AAEJcwwBQ7HNeuOmsYWAk6aqN2AAzEKanGk'
#bot = telepot.Bot(TOKEN)
#print (bot.getMe())


class MessageCounter(telepot.aio.helper.ChatHandler):
    def __init__(self, seed_tuple, timeout):
        super(MessageCounter, self).__init__(seed_tuple, timeout)
        self._count = 0 


    async def on_chat_message(self, msg):
        self._count += 1
        try:
            print ('Mandando mensaje')
            
            await self.sender.sendMessage(self._count)
            #loop.stop()
        except StopIteration as ex:
            salida = 'No ha más elementos en la cola'
            print (salida)

class TestClass():
    def __init__(self):
        print('Iniciando test')

    @asyncio.coroutine
    def test(self):
        while True:
             logger = logging.getLogger('simple_example')
             logger.debug('Test')
             #print ('TEST')
             yield from asyncio.sleep(2)



bot = telepot.aio.DelegatorBot(TOKEN, [
    (per_chat_id(), create_open(MessageCounter, timeout=10)),
])

logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

loop = asyncio.get_event_loop()
loop.create_task(bot.message_loop())
tst = TestClass()
loop.create_task(tst.test())

print('Listening ...')
logger.info('info message')
try:
    loop.run_forever()
finally:
    loop.close()
#input('Pulsa para salir')