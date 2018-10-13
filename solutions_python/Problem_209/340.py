
T = int(raw_input())

for t in xrange(T):

    N, K = map(int, raw_input().split())

    A = []
    H = []
    R = []
    for n in xrange(N):
        rad, height = map(float, raw_input().split())
        area = 3.14159265359 * rad ** 2
        height_cyl = 3.14159265359 * 2 * rad * height
        A.append(area)
        H.append(height_cyl)
        R.append(rad)

    best = 0.0
    for start in xrange(N):
        total =  A[start] + H[start]
        L = []
        for rest in xrange(N):
            if rest == start: continue
            if R[start] < R[rest]: continue
            L.append(H[rest])
        L = list(reversed(sorted(L)))
        total += sum(L[0:K-1])
        best = max(best, total)


    print 'Case #%d: %.9f' % (t+1, best)
