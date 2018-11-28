import sys

if len(sys.argv) < 2:
    print 'Usage saving.py inputfile'

f = open( sys.argv[1] )

def readln():
    return f.readline().strip()
    
    
nsets = int( readln() )
for i in xrange(0, nsets):
    nengines = int( readln() )
    engines = set([])
    for j in xrange(0,nengines):
        engines.add( readln() )
        
    nqueries = int( readln() )
    queries = []
    for j in xrange(0,nqueries):
        queries.append( readln() )
    
    # Find the longest distance until found
    running = True
    index = {}
    seen = set()
    switchcount = 0
    for count in xrange(0,nqueries):
        e = queries[count]
        if e not in engines or e in seen:
            continue
        index[e] = count
        seen.add(e)

        if seen == engines: #All engines were found
            index = {e:count}
            seen.clear()
            seen.add(e)
            switchcount += 1
    print 'Case #%d: %d'%(i+1,switchcount)