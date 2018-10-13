from __future__ import division
from operator import itemgetter

T = int(raw_input())

for test in xrange(T):
    N, V, X = raw_input().split()
    N = int(N)
    V = float(V)
    X = float(X)
    sources = []
    speed = 0.
    for i in xrange(N):
        R, C = [float(j) for j in raw_input().split()]
        if C == X:
            speed += R
        else:
            sources.append([R, C])
    sources.sort(key = itemgetter(1))
    cold = [0., 0.]
    hot = [0., 100.]
    while True:
        if cold[0] == 0.:
            if len(sources) == 0:
                break
            cold = sources.pop(0)
        if hot[0] == 0.:
            if len(sources) == 0:
                break
            hot = sources.pop()
        if cold[1] > X or hot[1] < X:
            break
        if (cold[0] * cold[1] + hot[0] * hot[1]) / (cold[0] + hot[0]) < X:
            speed += hot[0] + hot[0] * (hot[1] - X) / (X - cold[1])
            hot[0] = 0.
            cold[0] -= hot[0] * (hot[1] - X) / (X - cold[1])
        else:
            speed += cold[0] + cold[0] * (cold[1] - X) / (X - hot[1])
            cold[0] = 0.
            hot[0] -= cold[0] * (cold[1] - X) / (X - hot[1])

    ans = V / speed if speed != 0 else "IMPOSSIBLE"
    print "Case #{}: {}".format(test + 1, ans)
