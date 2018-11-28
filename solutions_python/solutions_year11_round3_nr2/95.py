from heapq import heappush, heappop
T  = int(raw_input())

for case in xrange(1,T+1):
    line = map(int, raw_input().split())
    L = line[0]
    t = line[1]
    N = line[2]
    C = line[3]

    dist=line[4:]*N
    dist=dist[:N]
    pDist = sum(dist)
    travelled = 0
    pos = 0
    time = 0
    ready = False
    index = 0
    for i in xrange(len(dist)):
        if not ready:
            if 2*dist[i] >= t:
                time += t
                travelled += 0.5*t
                ready = True
                dist[i] -= 0.5*t
                t = 0
                index = i
                break
            else:
                travelled += dist[i]
                time += 2*dist[i]
                t -= 2*dist[i]
                dist[i] = 0
    dist.sort()
    speed = 0
    L = min(L,len(dist))
    for i in xrange(-1,-1-L,-1):
        speed += dist[i]
    time += (speed) + 2*(pDist-travelled-speed)
    print "Case #%d: %d" %(case,time )
