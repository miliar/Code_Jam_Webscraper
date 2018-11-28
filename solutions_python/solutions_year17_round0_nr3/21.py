import sys
from collections import defaultdict

def split(gap):
    """Return size of big gap, small gap remaining"""
    # 1->0,0
    # 2->1,0
    # 3->1,1
    return gap//2, (gap-1)//2

def go(M):
    N,K = M.split()
    N = int(N)
    K = int(K)
    D = defaultdict(int) # Map from size of gap to count
    D[N] = 1
    while K>0:
        gap = max(D)
        count = D.pop(gap)
        count = min(K,count)
        assert count
        big,small = split(gap)
        D[big] += count
        D[small] += count
        K -= count
    return '{} {}'.format(big,small)
    
    
#sys.stdin=open('datac.txt')

T=input()
for t in range(1,T+1):
    M=raw_input()
    print "Case #{}: {}".format(t,go(M))
