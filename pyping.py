import sched
from pythonping import ping
import win32api

scheduler = sched.scheduler()


def pings():
    try:
        serv2 = ping("srv2.gestaopro.srv.br")
        serv3 = ping("srv3.gestaopro.srv.br")
        serv4 = ping("srv4.gestaopro.srv.br")
        serv5 = ping("srv5.gestaopro.srv.br")

        if serv2 or serv3 or serv4 or serv5:
            print('Tudo OK')
        elif serv2 != None:
            print('Servidor 2 Fora')
        elif serv3 != None:
            print('Servidor 3 Fora')
        elif serv4 != None:
            print('Servidor 4 Fora')
        elif serv5 != None:
            print('Servidor 5 Fora')

        scheduler.enter(delay=30, priority=0, action=pings)
        msgok = 'TUDO OK'
        win32api.MessageBox(0, msgok, f'SERVIDOR OK', 0x00001000)
    except RuntimeError:
        msgn = "Servidor Fora"
        win32api.MessageBox(0, msgn, f'SERVIDOR OK', 0x00001000)


pings()
scheduler.run(blocking=True)
