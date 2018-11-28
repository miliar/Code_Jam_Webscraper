import copy
import sys
from pprint import pprint

input = file(sys.argv[1])
count = int(input.readline())
i = 1

def parseMap(n, rows):
    map = [['.' for y in range(n)] for x in range(n)]
    for count, data in enumerate(rows):
        data = list(data)
        data.reverse()
        index = n - 1
        for val in data:
            if val == '.':
                continue
            else:
                map[count][index] = val
                index -= 1
    return map

def transformMap(map, direction):
    new_map = copy.deepcopy(map)
    to_add = range(len(map))
    index = range(len(map))
    if direction:
        index.reverse()
    for i, add in zip(index, to_add):
        new_map[i] = ['.' for ignore in range(add)] + new_map[i]
    return new_map

def findMatch(map, k):
    R = B = False
    for row in map:
        count = 0
        current = None
        for item in row:
            if item == current:
                count += 1
            else:
                count = 1 
                current = item
            if count == k:
                if current == 'R':
                    R = True
                elif current == 'B':
                    B = True
            if R and B:
                break
        if R and B:
            break
    for i in range(max([len(x) for x in map])):
        count = 0
        current = None
        for j in range(len(map)):
            try:
                item = map[j][i]
            except:
                item = '.'
            if item == current:
                count += 1
            else:
                count = 1
                current = item
            if count == k:
                if current == 'R':
                    R = True
                elif current == 'B':
                    B = True
            if R and B:
                break
        if R and B:
            break
    return R, B

while i <= count:
    bla = input.readline().strip()
    n, k = map(int, bla.split())
    mapx = []
    for ignore in range(n):
        mapx.append(input.readline().strip())
    mapx.reverse()
    mapx = parseMap(n, mapx)
    R, B = findMatch(mapx, k)
    if not (R and B):
        new_map1 = transformMap(mapx, False)
        a, b = findMatch(new_map1, k)
        R = a or R
        B = b or B
        if not (R and B):
            new_map2 = transformMap(mapx, True)
            a, b = findMatch(new_map2, k)
            R = a or R
            B = b or B
    if R:
        if B:
            result = 'Both'
        else:
            result = 'Red'
    else:
        if B:
            result = 'Blue'
        else:
            result = 'Neither'
    print 'Case #%i: %s' % (i, result)
    i += 1
