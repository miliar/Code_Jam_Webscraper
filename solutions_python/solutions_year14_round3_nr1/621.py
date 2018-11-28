from math import log, ceil
def readint():    return int(raw_input())
def readarray(f): return map(f, raw_input().split())

def solve(p, q):
    if int(log(q,2)) != log(q,2):
        q0 = q/p
        if q0*p != q:
            return "impossible"
        return int(log(q0,2))
    return int(ceil(log(q,2) - log(p,2)))

        

nb_cases = readint()
for test in xrange(nb_cases):
    line = raw_input().split('/')
    p = int(line[0])
    q = int(line[1])
    print "Case #%i:"% (test+1), solve(p,q)
