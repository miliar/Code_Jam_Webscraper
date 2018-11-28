import pickle, math
cache = dict()
STOP_AT = 9999999
DEBUG = 0
def parseInput(text):
    cases = []
    for i, line in enumerate(text.splitlines()):
        if i == 0 or i % 2 != 0:
            continue
        pancakes = [int(pan) for pan in line.split(' ')]

        cases.append(pancakes)
    return cases

def getOutput(solved):
    lines = []
    for i, solvedCase in enumerate(solved):
        lines.append("Case #%d: %d" % (i + 1, solvedCase))
    return '\n'.join(lines)

def generateOutput(filename, outFile = None):
    cases = getCases(filename)
    solvedCases = [naiveSolution(case) for case in cases]
    output = getOutput(solvedCases)
    if outFile == None:
        outFile = filename[:-2] + "out"
    with open(outFile, "w") as h:
        h.write(output)

    
def getCases(filename):
    with open(filename) as h:
        data = h.read()
    return parseInput(data)

def naiveSolution(dinersWithPancakes, t = 0, stopAt = None):
    global cache

    if stopAt is not None and t > stopAt:
        #print("stop: %d" % stopAt)
        return STOP_AT
    if t == 0:
        stopAt = max(dinersWithPancakes)
        #print (stopAt)
    dinersWithPancakes = sorted(dinersWithPancakes, reverse=True)

    ## Test in cache ##
    dinersWithPancakes = [pancakes for pancakes in dinersWithPancakes if pancakes != 0]

    cacheKey = ''.join((str(i) for i in sorted(dinersWithPancakes)))
    if cacheKey in cache:
        return t + cache[cacheKey]
    
    if len(dinersWithPancakes) == 0:
        return t

    eaten = [(pancakes - 1) for pancakes in dinersWithPancakes]
    if max(eaten) == 0:
        return t + 1

    res = []
        
    #for d, pancakes in enumerate(dinersWithPancakes):
    pancakes = dinersWithPancakes[0]
    d = 0
    for i in range(1, pancakes):
        test = dinersWithPancakes[:]
        test[d] -= i
        test.append(i)
        res.append(naiveSolution(test, t + 1, stopAt))
    #print("T: %d" % (t+1))
    res.append(t+pancakes)

    best = min(res)
    if best is not STOP_AT:
        cache[cacheKey] = best - t
    #print("Cached: cache['%s'] = %d" % (cacheKey, best - t))
    return best

def saveC(save = None):
    global cache
    with open("cache.obj", "wb") as h:
        pickle.dump(save if save is not None else cache, h)
def loadC():
    with open("cache.obj", "rb") as h:
        cache = pickle.load(h)
    return cache
