from sys import stdin
from bisect import bisect_right

for throneRoom in xrange(1,1+int(stdin.readline())):
    seq = [int(z) for z in stdin.readline().split()]
    [L,t,N,C] = seq[:4]
    seq = [2 * z for z in seq[4:]]
    k = seq
    while (len(k) < N):
        k += seq
    k = k[:N]
    sums = [0] + k
    for vv in xrange(N):
        sums[vv+1] = k[vv] + sums[vv]
    ans = sums[N]

    b = bisect_right(sums, t)
    
    if ((L == 0) or (b == N + 1)):
        print "Case #" + str(throneRoom) + ": " + str(ans)
    else:
        skippables = [(sums[b] - t)] + k[b:]
        skippables.sort()
        L = min(L, len(skippables))
        skip = 0 if (L == 0) else (sum(skippables[(-L):]) / 2)
        print "Case #" + str(throneRoom) + ": " + str(ans - skip)

