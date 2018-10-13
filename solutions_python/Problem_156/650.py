import math
cases = int(input())
for c in range(cases):
    x = map(int, input())
    y = map(int, input().split())
    y = sorted(y, reverse=True)
    m = y[0]
    res = y[0]
    for r in range(1, m + 1):
        move = 0
        for z in y:
            if z <= r:
                break
            move += math.ceil(float(z) / float(r)) - 1
        if move + r < res:
            res = move + r
    print('Case #%d: %d' % (c + 1, res))