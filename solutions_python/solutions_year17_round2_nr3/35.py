__author__ = 'sware'

import sys, collections, heapq

inputfile = file(sys.argv[1])
outputfile = file(sys.argv[2], 'w')

for case in xrange(int(inputfile.readline())):
    N,Q = map(int, inputfile.readline().split())
    horses = []
    distmatrix = []
    for _ in xrange(N):
        e,s = map(int, inputfile.readline().split())
        horses.append((e,s))
    for _ in xrange(N):
        distmatrix.append(map(int, inputfile.readline().split()))
    destinations = []
    for _ in xrange(Q):
        destinations.append(map(int, inputfile.readline().split()))
    thorsetimematrix = []
    for i in xrange(N):
        horsetimematrix = [-1 for _ in xrange(N)]
        tovisit = [(0,horses[i][0], i)]
        speed = float(horses[i][1])
        while tovisit:
            ti, e, place = heapq.heappop(tovisit)
            if horsetimematrix[place] != -1:
                continue
            horsetimematrix[place] = ti
            for j in xrange(N):
                dist = distmatrix[place][j]
                if dist == -1 or dist > e:
                    continue
                heapq.heappush(tovisit, (ti + float(dist) / speed, e-dist, j))
        thorsetimematrix.append(horsetimematrix)
    #print thorsetimematrix
    mintimes = []
    for start, dest in destinations:
        start -= 1
        dest -= 1
        visited = [-1 for _ in xrange(N)]
        tovisit = [(0, start)]
        while tovisit:
            ti, place = heapq.heappop(tovisit)
            #print ti, place
            if visited[place] != -1:
                continue
            visited[place] = 1
            if place == dest:
                mintimes.append(ti)
                break
            for j in xrange(N):
                nt = thorsetimematrix[place][j]
                if nt == -1:
                    continue
                heapq.heappush(tovisit, (ti + nt, j))
    outputfile.write('Case #{}: {}\n'.format(case+1, ' '.join(map(str, mintimes))))
outputfile.close()