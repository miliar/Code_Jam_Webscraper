'''
Created on Sep 3, 2009

@author: Robin
'''
import string

mapresult = []
pitcount = 96
def getneighbour(pos, map,w,h):
    values = [10000, 10000, 10000, 10000]
    if pos[0] > 0:
        values[0] = map[pos[0]-1][pos[1]]
    if pos[1] > 0:
        values[1] = map[pos[0]][pos[1]-1]
    if pos[1] < h-1:
        values[2] = map[pos[0]][pos[1]+1]
    if pos[0] < w-1:
        values[3] = map[pos[0]+1][pos[1]]
    #print values
    minpos = 0
    minval = values[0]
    for i in range(len(values)):
        if values[i] < minval:
            minval = values[i]
            minpos = i
    #print minpos
    if minpos == 1:
        return [pos[0], pos[1]-1]
    if minpos == 0:
        return [pos[0]-1, pos[1]]
    if minpos == 3:
        return [pos[0]+1, pos[1]]
    if minpos == 2:
        return [pos[0], pos[1]+1]
    
        
def rekurseDown(pos, map, w, h):
    global mapresult, pitcount
    if mapresult[pos[0]][pos[1]] != '.':
        return mapresult[pos[0]][pos[1]]
    n = getneighbour(pos, map, w, h)
    if map[pos[0]][pos[1]] <= map[n[0]][n[1]]:
        pitcount += 1
        return pitcount
    
    v = rekurseDown(n, map, w, h)
    mapresult[n[0]][n[1]] = v
    return v

f=open('a.in', 'r')
mapCount = int(f.readline())
maps = []
for i in range(mapCount):
    [w, h] = [int(x) for x in string.split(f.readline())]
    map = []
    mapresult = []
    pitcount = 0
    for y in range(w):
        map.append([int(x) for x in string.split(f.readline())])
        mapresult.append(['.' for x in map[y]])
    #print mapresult
    
    # iterate through map
    for row in range(len(mapresult)):
        for entry in range(len(mapresult[row])):
            if mapresult[row][entry] == '.':
                #print "neighbour of ",row," ",entry," is ",getneighbour([row, entry], map, w, h)
                mapresult[row][entry] = rekurseDown([row, entry], map, w, h)
    
    print "Case #"+str(i+1)+":"
    for y in mapresult:
        for x in y:
            print chr(x+96),
        print 
