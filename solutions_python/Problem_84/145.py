from heapq import *
t = int(raw_input())
for i in xrange(1,t+1):
    r, c = map(int,raw_input().split())
    grid = []
    blue = []
    good = True
    for j in xrange(r):
        grid.append(list(raw_input()))
        for k in xrange(c):
            if grid[j][k] == '#': heappush(blue,(j,k))
    while blue:
        x = heappop(blue)
        if grid[x[0]][x[1]] != '#': continue
        for j in [0,1]:
            for k in [0,1]:
                if x[0]+j < r and x[1]+k < c and grid[x[0]+j][x[1]+k] == '#':
                    grid[x[0]+j][x[1]+k] = '/' if (j+k)%2 == 0 else '\\'
                else:
                    good = False
            if not good: break
        if not good: break
    if not good: print "Case #%d:\nImpossible" % i
    else:
        print "Case #%d:" % i
        print "\n".join(map(lambda x: ''.join(x),grid))
