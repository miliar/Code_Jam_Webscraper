from __future__ import division

def solve():
    D,N = map(int, raw_input().split())
    horses = []
    for _ in xrange(N):
        Ki, Si = map(int, raw_input().split())
        horses.append((Ki, Si))
    horses.sort(reverse=True)

    farest = 0
    for h in horses:
        when = (D-h[0]) / h[1]
        farest = max(farest, when)

    return D/farest

T = int(raw_input())
for tt in xrange(T):
    print 'Case #{}: {}'.format(tt+1, solve())
