import math

C, F, X = 0, 0, 0

def farmtime(n):
     return C/(2+n*F)
def timeleft(n):
     return (X-C)/(2+n*F)
def fulltime(n):
     return X/(2+n*F)

def solve():
    n = 0
    speed = 2
    t = farmtime(n)
    while fulltime(n+1) < timeleft(n):
        t += farmtime(n+1)
        n += 1
    t += timeleft(n)
    return t

f = open("B-large.in", 'r')
testcases = int(f.readline())
for i in range(testcases):
    C, F, X = f.readline().split(' ')
    C = float(C)
    F = float(F)
    X = float(X)
    print "Case #%d: %.7f" % (i+1, solve())
