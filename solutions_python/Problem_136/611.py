import sys 
from math import *
lines = sys.stdin.readlines()
for i in range((int(lines[0]))):
    l = lines[i+1].split()
    C, F, X = float(l[0]), float(l[1]), float(l[2])
    if (X-C)/2 <= X/(2+F): print "Case #"+str(i+1)+": %5.7f" % float(X/2)
    else:
        N = ceil(X/C-2/F-1)
        t = 0.
        for j in range(int(N)): t += C/(2+F*j)
        t += X/(2+F*N)
        print "Case #"+str(i+1)+": %5.7f" % t
