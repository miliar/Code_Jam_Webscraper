#!/usr/bin/python
import sys

f=open(sys.argv[1],'r')
out=open(sys.argv[2],'w')

cases=int(f.readline().split()[0])
for case in xrange(cases):
    r,c,w=[int(x) for x in f.readline().split()]
    if w == 1:
        out.write("Case #{}: {}\n".format(case+1,r*c))
    else:
        total = (c-1)/w * r + w
        out.write("Case #{}: {}\n".format(case+1,total))


f.close()
out.close()
