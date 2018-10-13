from heapq import heappush as hpush, heappop as hpop, heapify

base = 100000000000

T = int(input())
for t in range(1, T+1):
    print("Case #%d: " % t, end="")
    n,k = map(int, input().split())
    u = int(float(input())*base)
    p = [int(base*float(x)) for x in input().split()]
    heapify(p)
    while u > 0:
        oldu = u
        small = hpop(p)
        poc = 1
        while len(p) > 0 and p[0] == small:
            poc += 1
            hpop(p)
        second = base if len(p) == 0 else p[0]
        rozdiel = second - small
        kolko = rozdiel
        if kolko*poc > u:
            kolko = u//poc
        co = min(small+kolko, base)
        u -= (co-small)*poc
        for i in range(poc):
            hpush(p, co)
        if oldu == u:
            break
    prod = 1.0
    for x in p:
        prod *= (x/(base+.0))
    print("%.6f" % prod)
