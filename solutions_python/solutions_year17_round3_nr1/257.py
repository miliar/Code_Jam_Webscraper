import math

t = int(raw_input())

for i in xrange(1, t + 1):
    n, k = [int(s) for s in raw_input().split(" ")]
    
    r = [0 for s in xrange(n)]
    h = [0 for s in xrange(n)]
    area = [0 for s in xrange(n)]
    
    def update(newR):
        for j in xrange(n):
            if newR > r[j]:
                area[j] = r[j] * h[j] * 2
            else:
                area[j] = r[j] * h[j] * 2 + r[j] * r[j] - newR * newR

    for j in xrange(n):
        r[j], h[j] = [int(s) for s in raw_input().split(" ")]
    
    baseR = 0
    update(baseR)
    sumH = 0
    
    for j in xrange(k):
        p = max(area)
        sumH = sumH + p
        idx = area.index(p)
        if r[idx] > baseR:
            baseR = r[idx]
            update(r[idx])
        area[idx] = 0
        r[idx] = 0
        h[idx] = 0
    
    sumH = sumH * math.pi
    
    print "Case #{}: {:0.7f}".format(i, sumH)
