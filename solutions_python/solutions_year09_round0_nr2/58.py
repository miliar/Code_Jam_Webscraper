import heapq
import sys
from collections import defaultdict

lines = sys.stdin.readlines()
T = int(lines[0])
line = 1
def read():
    global line
    l = lines[line]
    line += 1
    return l
def sp():
    return map(int, read().split(' '))

letters = 'abcdefghijklmnopqrstuvwxyz'

for problem in range(T):
    h, w = sp()
    mymap = defaultdict(dict)
    heap = []
    for j in range(h):
        l = sp()
        for i in range(w):
            mymap[i][j] = l[i], 0
            heapq.heappush(heap, (10000-l[i], i, j))

    def nexto(i, j):
        #N
        if j > 0:
            yield i, j-1
        if i > 0:
            yield i-1, j
        if i+1 < w:
            yield i+1, j
        #S
        if j+1 < h:
            yield i, j+1
    def neigh(i, j):
        for k, l in nexto(i, j):
            yield k, l, mymap[k][l]
    def lower(i, j, alt):
        plusbas = alt
        c = None
        for k, l, t in neigh(i,j):
            a, bas = t
            if a < plusbas:
                c = k,l, bas
                plusbas = a
        return c, plusbas
        
    sinks = 1
    print "Case #%d:" % (problem +1)
    while heap:
        alt, i, j = heapq.heappop(heap) 
        if mymap[i][j][1]:
            continue
        alt = 10000-alt
        ancestors = [(i,j)]

        down, alt2 = lower(i, j, alt)
        joined = False
        while down:
            mymap[i][j] = (alt, sinks)
            i, j, bas = down
            if bas:
                for i, j in ancestors:
                    mymap[i][j] = (mymap[i][j][0], bas)
                joined = True
                break    
            alt = alt2
            down, alt2 = lower(i, j, alt)
            ancestors.append((i,j))

        if joined:
            continue

        mymap[i][j] = (alt, sinks)

        sinks +=1

    rel = dict()
    cur = 0
    for j in range(h):
        for i in range(w):
            s = mymap[i][j][1]
            if s not in rel:
                rel[s] = letters[cur]
                cur += 1
            print rel[s],
        print
