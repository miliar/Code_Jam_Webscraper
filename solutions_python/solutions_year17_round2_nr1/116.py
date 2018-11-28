import sys
from collections import defaultdict

def run(D, N, H):
    m = 0
    for K, S in H:
        m = max(m, 1. * (D - K) / S)
    return 1.*D/m

f = file(sys.argv[1],'r')
T = int(f.readline().strip())
for case in range(1,T+1):
    D,N = [int(x) for x in f.readline().strip().split()]
    H = [[int(x) for x in f.readline().strip().split()] for i in range(N)]
    ans = run(D, N, H)
    print 'Case #%d: %.7f' % (case, ans)
