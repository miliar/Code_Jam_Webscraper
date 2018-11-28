import math

C = int(raw_input())

for case in xrange(1, C+1):
    N = int(raw_input())
    plants = [map(int, raw_input().split()) for _ in range(N)]
    best = float('Inf')
    if N < 3:
        best = max(r for x, y, r in plants)
    else:
        for i in range(N-1):
            for j in range(i+1, N):
                other = range(N)
                other.remove(i)
                other.remove(j)
                p1, p2, po = plants[i], plants[j], plants[other[0]]

                d = math.hypot(p1[0]-p2[0], p1[1]-p2[1])
                R = max((d+p1[2]+p2[2])/2.0, po[2])
    #            print i, j, R

                if R < best:
                    best = R

    print 'Case #%i: %.6f' % (case, best)
