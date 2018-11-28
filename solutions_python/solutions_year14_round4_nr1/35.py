import sys
from collections import deque


import psyco; psyco.full()

def main():
    f = open(sys.argv[1], "rb")
    ncases = int(f.readline())
    for caseno in xrange(ncases):
        a,b = f.readline().strip("\r\n").split()
        n = int(a)
        sz = int(b)
        
        ncds = 0
            
        files = []
        for a in f.readline().strip("\r\n").split():
            a = int(a)
            files.append(a)

        files.sort()
        
        while len(files) > 0:
            if len(files) >= 2 and files[-1] + files[0] <= sz:
                files.pop(0)
                files.pop()
                ncds += 1
            else:
                files.pop()
                ncds += 1
        
        print "Case #%d: %d" % (caseno+1, ncds)
        
main()