#!/usr/bin/python

def solve():
    X, S, R, t, N = [int(s) for s in raw_input().split()]
    walkways = []
    rest = X
    for i in range(N):
        begin, end, w = [int(s) for s in raw_input().split()]
        walkways.append((w, end - begin))
        rest -= end - begin
    if rest:
        walkways.append((0, rest))
    walkways.sort()
    result = 0
    for walkway in walkways:
        w = walkway[0]
        d = float(walkway[1])
        if t > 0:
            time = d / (R + w)
            if time <= t:
                result += time
                t -= time
            else:
                result += t + (d - (R + w) * t) / (S + w)
                t = 0
        else:
            result += d / (S + w)
    return result


T = int(raw_input())
for i in range(T):
    print 'Case #%d: %.6f' % (i + 1, solve())
