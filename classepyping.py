import sched
import schedule
import win32api
from pythonping import ping



scheduler = sched.scheduler()



def querySrv(srv):
    resp = ping(srv)
    if not resp:
        msgn = f'SERVIDOR {srv} CAIU'
        win32api.MessageBox(0, msgn, f'SERVIDOR {srv} FORA', 0x00001000)
        scheduler.enter(delay=30, priority=0, action=querySrv)



schedule.every(4).seconds.do(querySrv, 'srv2.gestaopro.srv.br')
schedule.every(7).seconds.do(querySrv, 'srv3.gestaopro.srv.br')
schedule.every(9).seconds.do(querySrv, 'srv4.gestaopro.srv.br')
schedule.every(11).seconds.do(querySrv, 'srv5.gestaopro.srv.br')

while True:
    schedule.run_pending()
