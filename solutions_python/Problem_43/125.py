import sys

from number import *

fdin = open(sys.argv[1],'r')
fdout = open(sys.argv[2],'w')

n = int(fdin.readline())
for i in range(n):
    line = fdin.readline().strip()
    fdout.write('Case #%d: %d\n' % ((i+1),doit(line)))

fdin.close()
fdout.close()
