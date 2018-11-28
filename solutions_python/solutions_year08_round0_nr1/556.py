
import sys
import re

def parse(data):
    result = []
    while len(data):
        engines = data[1:int(data[0]) + 1]
        data = data[int(data[0]) + 1:]
        queries = data[1:int(data[0]) + 1]
        data = data[int(data[0]) + 1:]
        result.append((engines, queries))
    return result

def bestEngines(engines, query):
    matches = {}
    for engine in engines:
        matches[engine] = 0
    for engine in engines:
        for e in query:
            if engine == e:
                break
            matches[engine] += 1
            
    items = matches.items()
    items.sort(cmp=lambda x,y: cmp(x[1], y[1]), reverse = True)
    return items[0][0]
        
def procced(engines, query):
    switch = 0
    engine = bestEngines(engines, query)
    while len(query):
        e = query.pop(0)
        if engine == e:
            engine = bestEngines(engines, [e] + query)
            switch += 1
    return switch
    
data = open(sys.argv[1]).read().split("\n")
cases = int(data[0])
result = parse(data[1:])
queries = result[:cases]

output = open(sys.argv[1].split(".")[0] + ".out", 'w')

case = 1
for engines, query in queries:
    i = procced(engines, query)
    print >> output, "Case #%d: %d" % (case, i)
    case += 1
    
output.close()
    