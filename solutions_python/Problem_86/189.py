fi=open("C-small-attempt0(1).in")
import re
import sys
T=int(fi.readline())
sys.stdout=open("C-small-attempt0(1).out","w")
def run(L,H,vs):
    for f in range(L,H+1):
        for v in vs:
            if not (v%f==0 or f%v==0):
                break
        else:
            return f
    return "NO"
for tn in range(T):
    N,L,H=map(int,fi.readline().split())
    vs=map(int,fi.readline().split())
    print "Case #%d:"%(tn+1),run(L, H, vs)
fi.close()
sys.stdout.close()