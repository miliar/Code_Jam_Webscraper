import math
import itertools
def exposedArea(l):
    return math.pi*(l[0]**2) + 2*math.pi*l[0]*l[1]

def sortf(li):
    return sorted(li,key=lambda l:l[0], reverse = True)
def farea(chosen):
    fareas = []
    for i in range(0, len(chosen)):
        fareas.append(exposedArea(chosen[i]))
        if i != 0:
            fareas[-1] -= math.pi*(chosen[i][0]**2)
    return sum(fareas)
t = int(input())
for test in range(1, t+1):
    data = [int (x) for x in input().split()]
    n = data[0]
    k = data[1]
    pancakes = []
    for i in range(0, n):
        pancakes.append([int (x) for x in input().split()])
    areas = []
    for i in range(0, n):
        areas.append(exposedArea(pancakes[i]))
##    if test == 16:
##    print(n, k)
##    print(pancakes)
##    print(areas)
    pos = []
    for i in range(0, k+1):
        for subset in itertools.combinations(pancakes, i):
            pos.append(list(subset))
##            print(subset)
##    print(itertools.combinations(pancakes, k))
##    print(pos)
##    print(sortf(pos[-1]))
    fas = []
    for i in range(0, len(pos)):
        fas.append(farea(sortf(pos[i])))
    
##    chosen = []
##    print(areas)
##    for i in range(0, k):
##        try:
##            if i != 0:
##    ##            print(pancakes[areas.index(max(areas))][0])
##    ##            print(chosen[i-1][0])
##                while pancakes[areas.index(max(areas))][0] > chosen[i-1][0]:
##                    del pancakes[areas.index(max(areas))]
##                    areas.remove(max(areas))
##        except ValueError:
##            pass
##        try:
##            chosen.append(pancakes[areas.index(max(areas))])
##            del pancakes[areas.index(max(areas))]
##            areas.remove(max(areas))
##        except ValueError:
##            pass
##    if test == 16:
##        print(chosen)
    
##    fareas = []
##    for i in range(0, len(chosen)):
##        fareas.append(exposedArea(chosen[i]))
##        if i != 0:
##            fareas[-1] -= math.pi*(chosen[i][0]**2)
##    print(fareas)
    
##    print(pancakes)
##    #print(exposedArea(pancakes[0]))
##    print(areas)
##    print(chosen)

##    print(fas)
    print("Case #" + str(test) + ": " + str(max(fas)))
