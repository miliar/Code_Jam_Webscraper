# Problem CodeJam 2010 1B - A
# Author John Schroder


tree = {}

def run( current, desired ):
    count = 0 
    current.sort()
    desired.sort()
    
    splitDesired = [ d.split("/")[1:] for d in desired if d not in current ]
    splitCurrent = [ c.split("/")[1:] for c in current ]
    splitDesired.sort()
    splitCurrent.sort()
    tree = { }
    for c in splitCurrent:
        level = tree
        for item in c:
            sublevel = level.get(item,{})
            level[item] = sublevel
            level = sublevel
            
    for d in splitDesired:
        level = tree
        for item in d:
            sublevel = level.get(item, None)
            if sublevel == None:
                count = count + 1
                sublevel = {}
                level[item] = sublevel
            level = sublevel
        
    return count

inputFile = "A-large.in"
outputFile = "A-large.out"
output = open(outputFile,"w")
input = open(inputFile,"r")

line = input.readline().strip()
nCases = int(line)
for nCase in range(1, nCases+1):
    tokens = input.readline().strip().split()
    N = int(tokens[0])
    M = int(tokens[1])
    current = []
    desired = []
    for n in range(N):
        current.append( input.readline().strip() )
    
    for m in range(M):
        desired.append( input.readline().strip() )

    print >> output, "Case #%d: %d" % ( nCase, run( current,desired ) )
    
output.close() 
