
import sys
from copy import deepcopy

input = open(sys.argv[1])
maps = int(input.readline().strip())
altitude = 0
altitude_map = {}
directions = [
        lambda x, y: (x, y - 1),
        lambda x, y: (x - 1, y),
        lambda x, y: (x + 1, y),
        lambda x, y: (x, y + 1)
        ]

for i in xrange(1, maps+1):
    print "Case #%s:" % i
    labels = list('abcdefghijklmnopqrstuvwxyz')
    h, w = [int(x) for x in input.readline().strip().split(' ')]
    map = [[int(x2) for x2 in input.readline().strip().split(' ')[:w]] for x in xrange(int(h))]
    original_map = deepcopy(map)

    depths = []
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            depths.append((cell, (x,y)))
    
    for depth, (x, y) in sorted(depths):
        top_diff = 0
        for direction in directions:
            nX, nY = direction(x, y)
            if nX < 0 or nY < 0: continue
            try:
                diff = original_map[y][x] - original_map[nY][nX]
                if map[nY][nX][0] == '#' and diff > top_diff:
                    map[y][x] = map[nY][nX]
                    top_diff = diff
            except IndexError: continue
            except TypeError: continue
            #if i == 2: print x,y,nX,nY,original_map[nY][nX],map[y][x]
        if isinstance(map[y][x], int):
            altitude += 1
            map[y][x] = '#%s' % altitude

    for row in map:
        row_vals = []
        for cell in row:
            if cell not in altitude_map:
                altitude_map[cell] = labels.pop(0)
            row_vals.append(altitude_map[cell])
        print ' '.join(row_vals)


