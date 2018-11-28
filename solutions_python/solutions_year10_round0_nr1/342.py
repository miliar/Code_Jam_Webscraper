from codejam import *

def run(f):
    n = int(f.next())
    k = int(f.next())
    if (k+1)&((1<<n)-1) == 0:
        print 'ON'
    else:
        print 'OFF'
    return

def main(fn):
    f=Reader(fn)
    n=int(f.next())
    for i in range(n):
        print 'Case #%d:'%(i+1), #TODO
        run(f)
    return

import sys
main(*sys.argv[1:])
