import math

for case in range(1, int(raw_input())+1):
    print "Case #%d: "%case, 
    n, k = map(int, raw_input().split())
    p = [map(int, raw_input().split()) for _ in range(n)]
    p.sort()
    p = map(lambda x: (math.pi*2*x[0]*x[1], x[0]), p)
    slist = []
    pre = ans = 0
    k -= 1
    if k == 0:
        ans = max(map(lambda x: x[0]+x[1]*x[1]*math.pi, p))
    else:
        for h, r in p:
            slist += [pre]
            if len(slist) > k:
                slist.remove(min(slist))
            ans = max(ans, sum(slist)+h+r*r*math.pi)
            pre = h

    print "%.9lf"%ans


        
