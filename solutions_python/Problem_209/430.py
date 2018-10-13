import math

T = int(raw_input())

for t in xrange(1, T + 1):
    N, K = map(int, raw_input().split())
    a = []
    for i in xrange(N):
        r, h = map(int, raw_input().split())
        v = 2 * r * h
        item = {'r' : r, 'v' : v}
        a.append(item)

    b = sorted(a, key=lambda k:k['v'], reverse=True)

    res = 0
    for i in xrange(N):
        k = 1
        total = b[i]['r'] * b[i]['r'] + b[i]['v']
        for j in xrange(N):
            if k == K:
                break
            if i == j or b[j]['r'] > b[i]['r']:
                continue
            k += 1
            total += b[j]['v']

        if res < total:
            res = total

    print "Case #%d: %f" % (t, res * math.pi)
