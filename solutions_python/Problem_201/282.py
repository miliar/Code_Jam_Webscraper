import heapq

def solve(N, K):
    h = [-N]
    counts = {N: 1}

    while K > 0:
        M = -heapq.heappop(h)
        D = counts[M]
        
        del counts[M]
        
        M -= 1

        if M % 2 == 0:
            ls = M / 2
            rs = M / 2
        else:
            ls = M / 2
            rs = (M + 1) / 2

        if ls in counts:
            counts[ls] += D
        else:
            heapq.heappush(h, -ls)
            counts[ls] = D

        if rs in counts:
            counts[rs] += D
        else:
            heapq.heappush(h, -rs)
            counts[rs] = D

        K -= D
    
    return str(max(ls, rs)) + ' ' + str(min(ls, rs))

def solve_small(N, K):
    stalls = [0] * N

    for i in xrange(K - 1):
        cur_l = None
        cur_r = None
        
        pass

T = int(raw_input())

for i in xrange(T):
    N, K = [int(x) for x in raw_input().split()]
    print 'Case #%d: %s' % (i + 1, solve(N, K))
    
