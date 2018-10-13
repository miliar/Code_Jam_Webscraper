
import sys
RL = lambda: sys.stdin.readline().strip()
IA = lambda: map(int, RL().split(" "))
LA = lambda: map(long, RL().split(" "))

T = int(sys.stdin.readline())

def mean(l):
    l = [x for x in l]
    x = len(l)
    return l[x/2]


def gcd(a,b):
    if a > b: return gcd(b,a)
    if b % a == 0: return a
    return gcd(b%a,a)
import math
for CASE in range(T):
    IMPOSSIBLE = "impossible"
    answer = 0
    p,q = map(int, RL().split("/"))

    while True:
        g = gcd(p,q)
        if g == 1: break
        p = p / g
        q = q / g
    n = 0
    if int(math.log(q,2)) != math.log(q,2):
        answer = IMPOSSIBLE
    else:
        answer = int(math.log(q,2) - int(math.log(p,2)))

    print "Case #%d: %s" % (CASE+1, answer)

