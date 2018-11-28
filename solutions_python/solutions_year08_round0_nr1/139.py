import sys
debug = False

def findengine( engines, queries ):
    workingengines = engines[:]
    
    for query in queries:
        if query in workingengines:
            workingengines.remove(query)
        if len(workingengines) == 1:
            break
        
    return workingengines[0]

def switcheroo( f ):
    changes = 0

    engines = [f.readline().rstrip() for i in range(int(f.readline()))]
    if debug: print engines
    
    queries = [f.readline().rstrip() for i in range(int(f.readline()))]
    if debug: print queries


    engine = findengine( engines, queries )

    while queries:
        for query in queries[:]:
            if query!=engine:
                queries.remove(query)
            else:
                break #out of the for loop, can't use current engine for next query
        if queries:
            changes += 1
            engine = findengine( engines, queries )
    
    return changes

if len(sys.argv) < 2:
    print "usage: %s inputfile [debug]" % sys.argv[0]
    exit()

if len(sys.argv) > 2:
    debug = sys.argv[2]
    
inputFile = sys.argv[1]

try:
    casefile = open( inputFile, "r" )
except:
    print "Error opening file: %s" % inputFile
    exit()

cases = int(casefile.readline())
for case in range(1,cases+1):
    changes = switcheroo( casefile )
    print "Case #%d: %d" % (case, changes)
