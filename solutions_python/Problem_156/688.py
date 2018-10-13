def f(s):
    return min(sum(z/i for z in s)+i for i in range(1,max(s)+2))
from sys import stdin
def r():
    return stdin.readline()
for cn in xrange(int(r())):
    d = r()
    print "Case #%d: %d"%(1+cn,f([int(z)-1 for z in r().split()]))
