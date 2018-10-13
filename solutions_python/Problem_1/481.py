#!/usr/bin/env python


f = "A-large.in"
# f = "A-large.in"

lines = open(f).read().split("\n")
index = 0


def getMaxValue(d):
    items = d.items()
    items.sort(key=lambda x: x[1])
    items.reverse()
    return items[0][1]
        

def read(how_many):
    global index
    global lines
    rtn = []
    for x in xrange(how_many):
        rtn.append(lines[index])
        index += 1
    if len(rtn) == 1: return rtn[0]
    return rtn
    

def valueExists(needle, haystack):
    for i in haystack.values():
        if needle == i:
            return True
    return False


def getDistance(engines, queries_left):
    d = {}    
    for i in engines:
        distance = 0
        for j in queries_left:
            if i == j:
                break
            distance += 1        
        if distance == len(queries_left):
            d[i] = -1
        else:
            d[i] = distance
    return d
        

def magic(engines, queries_left, count):
    distances = getDistance(engines, queries_left)
    
    while( not valueExists(-1, distances)):
        queries_left = queries_left[getMaxValue(distances):]
        count += 1
        distances = getDistance(engines, queries_left)
    
    return count
        

cases = int(read(1))
for i in range(cases):
    num_engines = int(read(1))
    engines = read(num_engines)
    num_queries = int(read(1))
    queries = read(num_queries)    
    
    print "Case #" + str(i + 1) + ": " + str(magic(engines, queries, 0))
