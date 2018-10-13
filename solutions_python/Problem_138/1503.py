import sys
import bisect

def war(optimizer, optimizee):
    optimizer = optimizer[:]
    optimizee = optimizee[:]

    ans = 0
    
    for n in optimizee:
        if n > optimizer[-1]:
            optimizer = optimizer[1:]
        else:
            ans += 1
            idx = bisect.bisect_left(optimizer, n)
            del optimizer[idx]
    return ans

T = int(sys.stdin.readline())
for t in range(T):
    N = int(sys.stdin.readline())
    strs = sys.stdin.readline()[:-1].split()
    naomi = [float(x) for x in strs]
    strs = sys.stdin.readline()[:-1].split()
    ken = [float(x) for x in strs]

    naomi = sorted(naomi)
    ken = sorted(ken)

    print "Case #%d: %d %d"%((t+1), war(naomi, ken), N - war(ken, naomi))
