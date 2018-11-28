import math

def solve(N, K):
    L = 2**int(math.log(K, 2))-1
    a = (N-L)%(L+1)
    if K-L <= a:
        return div((N-L)/(L+1) + 1)
    else:
        return div((N-L)/(L+1))
    
def div(n):
    return ' '.join([str(n/2), str((n-1)/2)])

for i in xrange(1, input()+1):
    l = raw_input().split()
    print "Case #%d: %s"%(i, solve(int(l[0]), int(l[1])))