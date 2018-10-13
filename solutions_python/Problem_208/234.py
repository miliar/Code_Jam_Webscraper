import copy

def calc(start, end, time, prehorse):
    if start == end:
        return time

    d = routes[start][start + 1]
    h = copy.copy(horses[start])
    h[0] -= d

    if prehorse == None:
        return calc(start+1, end, time + float(d)/h[1], h)
    else:
        prehorse = copy.copy(prehorse)
        prehorse[0] -= d


        x1 = x2 = None

        if h[0] >= prehorse[0] and h[1] >= prehorse[1]:
            return calc(start + 1, end, time + float(d) / h[1], h)
        elif h[0] <= prehorse[0] and h[1] <= prehorse[1]:
            return calc(start + 1, end, time + float(d) / prehorse[1], prehorse)

        if prehorse[0] >= 0:
            x1 = calc(start + 1, end, time + float(d) / prehorse[1], prehorse)
        if h[0] >= 0:
            x2 = calc(start + 1, end, time + float(d) / h[1], h)

        if x1 != None and x2 != None:
            return min(x1, x2)
        elif x1 == None:
            return x2
        else:
            return x1


T = int(raw_input())

for t in xrange(T):

    N, Q = map(int, raw_input().split())

    routes = []
    horses = []

    for n in xrange(N):
        maxdist, speed = map(int, raw_input().split())
        horses.append([maxdist, speed])

    for n in xrange(N):
        routes.append(map(int, raw_input().split()))

    ans = []

    for q in xrange(Q):
        start, end = map(int, raw_input().split())

        ans.append(calc(start-1, end-1, 0.0, None))

    print "Case #" + str(t+1) + ": " + ' '.join(map(str, ans))