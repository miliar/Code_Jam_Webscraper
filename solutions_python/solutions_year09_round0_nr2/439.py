#! /usr/bin/python
import sys
from collections import deque

# Direction: 0:basin 1:right 2:down 3:legt 4:up
def get_drain_map(map):
    height = len(map); width = len(map[0]);
    drain_map = [['' for i in range(width)] for i in range(height)]
    marker = 'a'
    for x in range(height):
        for y in range(width):
            if drain_map[x][y] != '':
                continue
            mark_region(x, y, marker, map, drain_map, width, height);
            marker = chr(ord(marker) + 1)
    return drain_map

def mark_region(x, y, marker, map, drain_map, width, height):
    basin = deque()
    basin.append((x, y))
    drain_map[x][y] = marker
    directions = [(-1,0), (0,-1), (0,1), (1,0)]
    while len(basin) > 0:
        (a, b) = basin.pop()
        lowest = map[a][b]
        for d in directions:
            if a+d[0]>=0 and a+d[0]<height and b+d[1]>=0 and b+d[1]<width:
                if map[a+d[0]][b+d[1]] < lowest:
                    lowest = map[a+d[0]][b+d[1]]
                    to_dir = d
                if map[a+d[0]][b+d[1]] > map[a][b]:
                    from_dir = d
                    self_found = False
                    for td in directions:
                        if td[0] == -d[0] and td[1] == -d[1]:
                            self_found = True
                        if a+d[0]+td[0]>=0 and a+d[0]+td[0]<height and b+d[1]+td[1]>=0 and b+d[1]+td[1]<width:
                            if map[a+d[0]+td[0]][b+d[1]+td[1]] < map[a][b]:
                                from_dir = False
                            if self_found == False and map[a+d[0]+td[0]][b+d[1]+td[1]] == map[a][b]:
                                from_dir = False
                    if from_dir != False and drain_map[a+from_dir[0]][b+from_dir[1]] == '':
                        basin.append((a+from_dir[0], b+from_dir[1]))
                        drain_map[a+from_dir[0]][b+from_dir[1]] = marker
        if lowest < map[a][b] and drain_map[a+to_dir[0]][b+to_dir[1]] == '':
            basin.append((a+to_dir[0], b+to_dir[1]))
            drain_map[a+to_dir[0]][b+to_dir[1]] = marker

                    

if __name__ == "__main__":
    input_file = sys.argv[1]
    data = open(input_file)
    cases = int(data.readline().strip())
    for i in range(cases):
        x, y = data.readline().strip().split()
        map = []
        for counter in range(int(x)):
            row = data.readline().strip().split()
            map.append([row[it] for it in range(int(y))])
        drain_map = get_drain_map(map)
        print "Case #%d:" % (i+1,)
        for counter in range(int(x)):
            print ' '.join(drain_map[counter])