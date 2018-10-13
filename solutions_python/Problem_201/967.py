import sys
from collections import defaultdict
rl = lambda : sys.stdin.readline().strip()

ncase = int( rl() )

for caseno in xrange(1,ncase+1):
    n, k = map(int,rl().split())

    x = defaultdict(int)
    x[n] = 1

    tot = 0
    ans = ""

    if k == 1:
        if n % 2 == 0:
            ans = "{} {}".format(n/2,n/2-1)
        else:
            ans = "{} {}".format(n/2,n/2)
    else :
        for i in xrange(1000):
            if tot+2**i >= k:
                tmp = tot
                for t in sorted(x.keys())[::-1]:
                    if tmp+x[t]>=k:
                        if t % 2 == 0:
                            ans = "{} {}".format(t/2,t/2-1)
                        else:
                            ans = "{} {}".format(t/2,t/2)
                        break
                    tmp += x[t]
                break
            
            y = defaultdict(int)
            tot += 2**i
            for t, v in x.items():
                if t % 2 == 0:
                    y[t/2] += v 
                    y[t/2-1] += v 
                else:
                    y[t/2] += v 
                    y[t/2] += v 
            x = y
    print "Case #{}: {}".format(caseno, ans)
