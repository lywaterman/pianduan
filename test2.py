import time
import logging
import logging.handlers
from daemon import runner

class App():

    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path =  '/tmp/foo.pid'
        self.pidfile_timeout = 5

    def run(self):
        logs = logging.getLogger('MyLogger')
        logs.setLevel(logging.DEBUG)
        fh = logging.handlers.RotatingFileHandler(
            '/tmp/test.log',maxBytes=10000000,backupCount=5)
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter(u'%(asctime)s [%(levelname)s] %(message)s')
        fh.setFormatter(formatter)
        logs.addHandler(fh)
        from subprocess import Popen, PIPE, CalledProcessError

        cmd = ["/usr/local/Cellar/iftop/1.0pre4/sbin/iftop", "-t"]
        with Popen(cmd, stdout=PIPE, bufsize=1, universal_newlines=True) as p:
            for line in p.stdout:
                logs.info(line) # process line here

            if p.returncode != 0:
                raise CalledProcessError(p.returncode, p.args)

        #while True:
        #    for i in range(10):
        #        logs.info("Beginning Scan {0}! \n".format(i))
        #    time.sleep(1)

app = App()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
