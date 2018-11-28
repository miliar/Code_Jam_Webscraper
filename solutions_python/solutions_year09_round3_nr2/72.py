import sys

from fire import *

fdin = open(sys.argv[1],'r')
fdout = open(sys.argv[2],'w')

n = int(fdin.readline())
for i in range(n):
    nline = int(fdin.readline())
    plist = []
    for j in range(nline):
        line = fdin.readline().strip().split()
        line = [int(x) for x in line]
        plist.append(line)
    dmin,t = return_min(plist)
    fdout.write('Case #%d: %.8f %.8f\n' % ((i+1), dmin, t))

fdin.close()
fdout.close()
