def istidy(x):
    return "".join(sorted(x)) == x

def solve(n):
    if n < 10:
        return n
    n = str(n)

    best = ""
    
    if istidy(n): return n

    for i in xrange(len(n)):
        cand1 = n[:i+1] + "9" * (len(n)-i-1)
        if istidy(cand1) and cand1 <= n:
            if best<cand1: best = cand1

        if ( i > 0 and n[i] > n[i-1] ) or ( i == 0 and n[i] > '1' ):
            cand2 = list(n[:i+1] + "9" * (len(n)-i-1))
            cand2[i] = int(cand2[i])
            cand2[i] -= 1
            cand2[i] = str(cand2[i])
            cand2 = "".join(cand2)

            if istidy(cand2) and cand2 <= n:
                if best<cand2: best = cand2


    if len(best)>0: return best
    return "9" * (len(n)-1)

import sys

rl = lambda : sys.stdin.readline().strip()

ncase = int( rl() )

for caseno in xrange(1,ncase+1):
    n = int(rl())
    print "Case #{}: {}".format(caseno, solve(n))
