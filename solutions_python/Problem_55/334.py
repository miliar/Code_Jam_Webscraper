import fileinput
import psyco
psyco.full()

def generateCounters(g,k):
    """
    Plan here: get an array telling us which will be the next index
    if we start at a specific point, and how many people we will get
    on the train. Basic Dynamic Programing.
    Later on, figure out what states we go through (loop's max length is N),
    and figure out how many iterations there are.
    """
    # Complexity for this function - O(N^2)
    for x in range(len(g)):
        s = 0
        y = x
        # Check for wrap around situations, account for them
        if k > sum(g):
            yield (x, sum(g))
            continue
        # At most O(N) iterations here
        while (s + g[y]) <= k:
            s += g[y]
            y = (y+1)%len(g)
        yield (y,s)


def findLoop(g,k,R,counters):
    visitedLocations = set()
    currentLocation = 0
    initialCount = 0
    stepsCounter = 0

    # Prolog
    while currentLocation not in visitedLocations:
        visitedLocations.add(currentLocation)
        initialCount += counters[currentLocation][1]
        currentLocation = counters[currentLocation][0]
        stepsCounter += 1
        if stepsCounter == R:
            #print "Prolog exit"
            return initialCount

    # Loop re-rolling
    loopPoint = currentLocation
    loopSteps = 1
    loopCount = counters[currentLocation][1]
    currentLocation = counters[currentLocation][0]
    while loopPoint != currentLocation:
        #print "looping"
        loopSteps += 1
        loopCount += counters[currentLocation][1]
        currentLocation = counters[currentLocation][0]
        
    fullLoops = (R - stepsCounter) / loopSteps
    loopsCount = loopCount * fullLoops
    #print fullLoops
    
    # epilog
    endSteps = R - stepsCounter - loopSteps*fullLoops
    endCount = 0
    #print endSteps
    for x in range(endSteps):
        #print "epilog"
        endCount += counters[currentLocation][1]
        currentLocation = counters[currentLocation][0]

    return initialCount + loopsCount + endCount

def main():
    it = fileinput.input()
    it.next()
    for (case,l) in enumerate(it):
        (R,k,N) = [int(x) for x in l.split()]
        g = [int(x) for x in it.next().split()]
        print "Case #%d: %d" %(case+1,findLoop(g,k,R,list(generateCounters(g,k))))

if __name__ == "__main__":
    main()
    
