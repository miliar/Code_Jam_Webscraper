#!/usr/bin/python

import sys
from math import sqrt
import mpmath
from copy import deepcopy

#############################

dynamic_map={}
def dynamic(func):
    def decorator(*args, **kwargs):
        if (func,args) in map:
            return map[(func,args)]
        else:
            r = func(*args, **kwargs)
            map[(func,args)] = r
            return r
    return decorator

#############################

















#############################

fd = open(sys.argv[1])
out = []
for I_line in xrange(int(fd.readline()[:-1])):
    line = fd.readline()[:-1].split(" ")







    [N,M,A] = map(int, line)

    found = False
    out_s = "IMPOSSIBLE"
    for x2 in xrange(1,N+1):
        if found:
            break
        for x3 in xrange(N+1):
            if found:
                break
            for y2 in xrange(M+1):
                if found:
                    break

                if (A+y2*x3)%x2 == 0:
                    y3 = (A+y2*x3)/x2 
                    if y3 <=M:
                        out_s="0 0 %d %d %d %d"%(x2,y2,x3,y3)
                        found = True










    ################
    out_str="Case #%d: %s"%(I_line+1,out_s)
    print out_str
    out.append(out_str)



fd.close()

fd = open(sys.argv[2],"w")
fd.write("\n".join(out))
fd.close()


