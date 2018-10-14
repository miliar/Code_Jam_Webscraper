import math
import shlex

from sys import stdin
def rline():
    return stdin.readline().rstrip()

a = {}
def isP(n):
    s = str(n)
    for i in range(0, len(s)/2):
        if s[i] != s[-i-1]:
            return False
    return True

def go(s, e):
    c = 0
    s = int(math.ceil(math.sqrt(s)))
    e = int(math.floor(math.sqrt(e)))
    # print "%d,%d"%(s,e)
    for i in range(s, e+1):
        try:
            a[i]
        except KeyError:
            if isP(i) and isP(int(math.pow(i, 2))):
                a[i] = True
            else:
                a[i] = False
        if a[i]:
            c=c+1
    return c

for l in range(int(rline())):
    (n,m) = map(int, rline().split())
    # print "%d,%d"%(n,m)
    print "Case #%d: %d"%(l+1, go(n, m))


