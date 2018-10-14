import sys
import re

def fact(x):
    return reduce(lambda i,j : i*j, range(1,x+1))

def goro_sort(ar):
    sar = sorted(ar)
    c = 0
    for i in range(len(ar)):
        if sar[i] == ar[i] :
            c += 1
    return len(ar)-c
   
for k in range(1, int(sys.stdin.readline())+1):
    line = sys.stdin.readline().rstrip().split()
    line = sys.stdin.readline().rstrip().split()
    
    ar = []
    for l in line:
        ar.append(int(l))
    
    print "Case #%d: %d"%(k, goro_sort(ar))
    