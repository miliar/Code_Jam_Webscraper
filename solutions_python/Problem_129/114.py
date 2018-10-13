from __future__ import division
from collections import defaultdict

def price(a):
    global n
    s, e, p = a
    l = e-s+1
    return (l+1)*(n-l/2)*p

def cheat(d):
    t = []
    for s, e, p in d:
        t += [(s, False, p), (e, True, p)]
    t.sort()

    r = []
    lst = defaultdict(int)
    for st, ex, num in t:
        if not ex:
            lst[st] += num
        else:
            k = sorted(lst.keys(), reverse=True)
            c = 0
            i = 0
            while c < num:
                if lst[k[i]] > num - c:
                    lst[k[i]] -= num - c
                    r += [(k[i], st, num-c)]
                    c = num
                else:
                    c += lst[k[i]]
                    r += [(k[i], st, lst[k[i]])]
                    del lst[k[i]]
                i += 1
    return r
        

t = int(raw_input())
for c in range(t):
    n, m = map(int, raw_input().split())
    d = []
    for i in range(m):
        d.append(map(int, raw_input().split()))

    city = sum(map(price, d))
    d = cheat(d)
    people = sum(map(price, d))

    print "Case #{0}: {1:.0f}".format(c+1, city-people)
