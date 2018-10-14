from math import ceil

def choc(p, groups):
    chocs = []
    for i in range(p):
        chocs.append(0)

    for i in groups:
        j = i%p
        chocs[j] = chocs[j] + 1

    if p == 2:
        return int(chocs[0] + ceil(chocs[1]/2.))

    if p == 3:
        a = min(chocs[1],chocs[2])
        b = max(chocs[1],chocs[2])
        return int(chocs[0] + a + ceil((b-a)/3.))


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t+1):
    n, p = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    groups = [int(s) for s in raw_input().split(" ")]
    print "Case #{}: {}".format(i, choc(p, groups))