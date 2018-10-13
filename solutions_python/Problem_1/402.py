def sortedDictValues3(adict):
    keys = adict.keys()
    keys.sort()
    return map(adict.get, keys)


f = open("C:\SAVING5.TXT")

lines = f.read().split("\n")

times= int(lines[0])
lines = lines[1:]

for x in xrange(times):
    engines = []
    searches = []
    enginecount = int(lines[0])
    lines = lines[1:]
    for y in xrange(enginecount):
        engines.append(lines[y])
    lines = lines[enginecount:]
    
    start = int(lines[0])
    searches = lines[1:int(lines[0])+1]
    lines = lines[1:]
    
    dist = {}
    switches = -1
    while True:
        for engine in engines:
            if engine in searches:
                dist[engine] = searches.index(engine)
            else:
                dist[engine] = -1
        
    
        m = dist.values()
        m.sort()
        
        if m[0] == -1:
            switches += 1
            break
        switches += 1
        searches = searches[m[len(m)-1]:] #check this for errors
        
    print "Case #" + str(x+1) + ": " + str(switches)
    lines = lines[start:]