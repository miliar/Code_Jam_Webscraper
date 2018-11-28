from heapq import heappush as push, heappop as pop

def solver(Hs, Ds):
    N = len(Hs)
    times = {(i, i):0 for i in xrange(N)}
    for i in xrange(N-1):
        D = 0
        e, s = Hs[i]
        for j in xrange(i+1, N):
            D += Ds[j-1][j]
            if D <= e:
                times[(i, j)] = D / s
            else:
                times[(i, j)] = float('inf')
    for i in xrange(N-2, -1, -1):
        for j in xrange(i+1, N):
            times[(i, j)] = min([times[(i,k)] + times[(k,j)] for k in
            xrange(i+1, j+1)])
    return times[(0, N-1)]


def main(index):
    print 'Case #%d:' % index,
    N, Q = map(int, raw_input().split())
    Hs = [map(float, raw_input().split()) for i in xrange(N)]
    Dis = [map(float, raw_input().split()) for i in xrange(N)]
    Des = [map(int, raw_input().split()) for i  in xrange(Q)]

    print '%.6f' % solver(Hs, Dis)

    
T = int(raw_input())
for i in xrange(1, T+1):
    main(i)
