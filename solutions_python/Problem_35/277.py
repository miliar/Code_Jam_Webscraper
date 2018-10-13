#!/usr/bin/env python

T = int(raw_input())


for case in xrange(1, T+1):
    H, W = map(int, raw_input().split())
    world = [[0]*(H+2) for i in xrange(W+2)]
    basin = [['*']*(H+2) for i in xrange(W+2)]
    max_height = 0
    for y in xrange(1, H+1):
        line = map(int, raw_input().split())
        max_height = max(max_height, max(line))
        for x in xrange(W):
            world[x+1][y] = line[x]
    max_height += 1

    for x in xrange(W+2):
        world[x][0] = max_height
        world[x][H+1] = max_height
    
    for y in xrange(1,H+1):
        world[0][y] = max_height
        world[W+1][y] = max_height

    for y in xrange(1, H+1):
        for x in xrange(1, W+1):
            if world[x][y] <= min(world[x+1][y],world[x-1][y],
                                  world[x][y+1],world[x][y-1]):
                basin[x][y] = '.'

    curletter = 'a'
    def dfs(x, y):
        global curletter
        moves = [(0,-1), (-1,0), (1,0), (0,1)]
        if ord(basin[x][y]) >= ord('a') and \
            ord(basin[x][y]) <= ord('z'):
            return basin[x][y]
        elif basin[x][y] == '.':
            basin[x][y] = curletter
            curletter = chr(ord(curletter)+1)
            return basin[x][y]
        elif basin[x][y] == '*':
            min_alt = min([world[x+x1][y+y1] for x1, y1 in moves])
            for x1, y1 in moves:
                if world[x+x1][y+y1] == min_alt:
                    basin[x][y] = dfs(x+x1, y+y1)
                    break
            return basin[x][y]
        else:
            raise "fail"

    for y in xrange(1, H+1):
        for x in xrange(1, W+1):
            dfs(x,y)

    print "Case #%d:" % (case)
    for y in xrange(1, H+1):
        line = []
        for x in xrange(1, W+1):
            line.append(basin[x][y])
        print ' '.join(line)
            
