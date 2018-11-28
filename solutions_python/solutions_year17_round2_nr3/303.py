from collections import defaultdict
from Queue import PriorityQueue as PQ
T = input()
#T = 1
for test in xrange(1, T+1):
    N, Q = map(int, raw_input().split())
    #Q = 1
    # E S
    horses = [map(int, raw_input().split()) for x in xrange(N)]
    #print horses
    #adj = [map(int, raw_input().split()) for x in xrange(N)]
    edges = defaultdict(dict)
    for i in xrange(N):
        for j, v in enumerate(raw_input().split()):
            if int(v) != -1:
                edges[i][j] = int(v)
    routes = [map(int, raw_input().split()) for x in xrange(Q)]
    pq = PQ()
    results = []
    for u, v in routes:
        u -= 1
        v -= 1
        #print u, v
        #ests = defaultdict(lambda:float("inf"))
        seen = set()
        pq.put((0., u, horses[u][0], u))
        while not pq.empty():
            cost, curr, left, horse = pq.get(False)
            if (curr, horse) in seen:
                continue
            seen |= {(curr, horse)}
            speed = horses[horse][1]
            newLeft, newSpeed = horses[curr]
            #print
            #print 'p', curr, cost, left, speed, seen, horse
            if curr == v:
                #print 'found', v, cost
                results.append(cost)
                break
            for dest in edges[curr]:
                oldDestCost = cost + edges[curr][dest]/float(speed)
                newDestCost = cost + edges[curr][dest]/float(newSpeed)
                #print 'd', dest, left, newLeft,
                if left >= edges[curr][dest]:
                    #ests[dest] = oldDestCost
                    #print oldDestCost,
                    pq.put((oldDestCost, dest, left-edges[curr][dest], horse))
                if newLeft >= edges[curr][dest]:
                    #ests[dest] = newDestCost
                    #print newDestCost,
                    pq.put((newDestCost, dest, newLeft-edges[curr][dest], curr))
                #print
                
    #print results
    print ("Case #%d:"+" %f"*Q)%((test,) + tuple(results))
