from sys import *
from string import rfind
import re

t = int(stdin.readline())
for i in xrange(1,t+1):
    direc = set(['/', ''])
    count, bak = 0, 0
    nm = re.split(' ', stdin.readline())
    n, m = int(nm[0]), int(nm[1])
    for j in xrange(n):
        l = stdin.readline()
        direc.add(l[0:-1])
#    print direc
    for j in xrange(m):
        req = stdin.readline()[0:-1]
        bak = 0
        index = 0
        while req not in direc:
            bak += 1
     #       print bak, req
            direc.add(req)
            index = rfind(req, "/")
            req = req[:index]
        count += bak
    print "Case #%(i)d: %(count)d" % locals()

