import sys
from heapq import *

f = open(sys.argv[1])

t = int(f.readline())
for case in range(t):
    n = int(f.readline())
    levels = []
    for i in range(n):
        a, b = map(int, f.readline().split(" "))
        levels.append((i, a,b))


    #first, provide two sortings
    by_first = levels[:]
    by_first.sort(key=lambda (i,x,y):x)

    remaining = by_first

    
    q = []
    stars = 0
    i = 0
    inq = set()
    while True:
        l, s1, s2 = by_first[i]
        if s2 == stars:
            heappush(q, (1, 2, set([(l, 2), (l, 1)])))
        elif s1 == stars:
            heappush(q, (1, 1, set([(l, 1)])))
        else:
            break
        i += 1
        if i == len(by_first):
            break
    
    result = 4000
    while q:
        cost, stars, seen = heappop(q)

        if len(seen) == len(by_first)*2:
            result = cost
            break
        for level, s1, s2 in by_first:
            if not (level, 2) in seen and s2 <= stars:
                    value = 2
                    newseen = set(seen)
                    newseen.add((level, 2))
                    if (level, 1) in seen:
                        value = 1
                    else:
                        newseen.add((level, 1))
                    state = (cost + 1, stars+value,frozenset(newseen))
                    if state in inq:
                        continue
                    heappush(q, state)
                    inq.add(state)
            elif not (level, 1) in seen:
                if s1 <= stars:
                    newseen = set(seen)
                    newseen.add((level, 1))
                    state = (cost + 1, stars+1,frozenset(newseen))
                    if state in inq:
                        continue
                    heappush(q, state)
                    inq.add(state)

    if result == 4000:
        result = "Too Bad"
    print "Case #%d: %s" % (case+1, result)
