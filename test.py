from subprocess import Popen, PIPE, CalledProcessError

cmd = ["/usr/local/Cellar/iftop/1.0pre4/sbin/iftop", "-t"]
with Popen(cmd, stdout=PIPE, bufsize=1, universal_newlines=True) as p:
    for line in p.stdout:
        print(line, end='') # process line here

if p.returncode != 0:
    raise CalledProcessError(p.returncode, p.args)
