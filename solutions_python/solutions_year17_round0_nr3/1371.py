import multiprocessing as mp

def solve(N, K):
    def Ls(b, s):
        for i, stall in enumerate(b[:s][::-1]):
            if stall == 'o':
                return i
    def Rs(b, s):
        for i, stall in enumerate(b[s+1:]):
            if stall == 'o':
                return i
    def brute_force(N, K):
        b = ['o']+['.' for _ in range(N)]+['o']
        for i in xrange(1, K+1):
            choose = 1
            minLR = 0
            maxLR = 0
            for s in range(1, len(b)-1):
                if b[s] == 'o':
                    continue
                L, R = (Ls(b, s), Rs(b, s))
                if minLR < min(L, R):
                    minLR = min(L, R)
                    maxLR = max(L, R)
                    choose = s
                elif minLR == min(L, R) and maxLR < max(L, R):
                    maxLR = max(L, R)
                    choose = s
                elif minLR == min(L, R) and maxLR == max(L, R) and s < choose:
                    choose = s
            b[choose] = 'o'
            #print b
            if i == K:
                return maxLR, minLR
    def greedy(N, K):
        import heapq as hq
        bb = [-N]
        for i in xrange(1, K+1):
            #print bb
            n = hq.heappop(bb)
            n2 = -((-n)/2)
            if n2 < 0:
                hq.heappush(bb, n2)
            if n-n2+1 < 0:
                hq.heappush(bb, n-n2+1)
            if i == K:
                return -(n2), -(n-n2+1)
    return '%d %d' % greedy(N, K)

if __name__ == '__main__':
    pool = mp.Pool(mp.cpu_count())
    case_num = int(raw_input())
    results = []
    for i in range(1, case_num+1):
        N, K = raw_input().split()
        results.append(pool.apply_async(solve, args=(int(N), int(K), )))
    output = [p.get() for p in results]
    pool.close()
    pool.join()
    for i,out in enumerate(output):
        print 'Case #%d: %s' % (i+1, str(out))
