import sched
from pythonping import ping
import win32api
from datetime import datetime


data = datetime.now()
data_hora = data.strftime("%d/%m/%y %H:%M")
data = data.strftime("%d/%m/%y")


scheduler = sched.scheduler()


def srv2():
    msg = 'SRV2 OFFLINE'
    if not ping('srv2.gestaopro.srv.br'):
        win32api.MessageBox(0, msg, 'SRV2 OFFLINE', 0x00001000)
    scheduler.enter(delay=5, priority=0, action=srv2)


def srv3():
    msg = 'SRV3 OFFLINE'
    if not ping('srv3.gestaopro.srv.br'):
        win32api.MessageBox(0, msg, 'SRV3 OFFLINE', 0x00001000)
    scheduler.enter(delay=7, priority=2, action=srv3)


def srv4():
    msg = 'SRV4 OFFLINE'
    if not ping('srv4.gestaopro.srv.br'):
        win32api.MessageBox(0, msg, 'SRV4 OFFLINE', 0x00001000)
    scheduler.enter(delay=9, priority=4, action=srv4)


def srv5():
    msg = 'SRV5 OFFLINE'
    if not ping('srv5.gestaopro.srv.br'):
        win32api.MessageBox(0, msg, 'SRV5 OFFLINE', 0x00001000)
    scheduler.enter(delay=11, priority=6, action=srv5)


def start():
    scheduler.enter(delay=5, priority=0, action=srv2)
    scheduler.enter(delay=7, priority=2, action=srv3)
    scheduler.enter(delay=9, priority=4, action=srv4)
    scheduler.enter(delay=11, priority=6, action=srv5)


start()
scheduler.run(blocking=True)
