# 27 = esc
# 299 lewo
# 301 prawo
# 296 gora
# 304 dol
# pip install py-getch
from multiprocessing.dummy import Process, Value
import os
import getch
import time
wait = lambda:time.sleep(0.5)
clear_console = lambda: os.system('cls')
class get_key:
    key = Value('d', 0)
    key2 = Value('d', 0)
    p = None
    def __init__(self):
        self.p = Process(target=self.GetKeyThread, args=(self.key,))
        self.p.start()
    def GetKeyThread(self, key):
        while True:
            key.value = ord(getch.getch())
            if key.value == 224:
                key.value = key.value + ord(getch.getch())
            if key.value == 27:
                break
    def __call__(self):
        value = self.key.value
        self.key.value = 0
        return value





















