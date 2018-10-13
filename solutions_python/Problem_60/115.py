import sys


def main(fName):
    f = open(fName, "r")
    cases = int(f.readline())
    for caseNum in xrange(cases):
        numberOfChicks, chickLimit, barnLocation, timeLimit = map(int, f.readline().split())
        locations = map(int, f.readline().split())
        speeds = map(int, f.readline().split())
        chicks = zip(locations, speeds)
        possibleCount = 0
        for chick in chicks:
            if wouldMakeIt(chick, barnLocation, timeLimit):
                possibleCount += 1
        if possibleCount < chickLimit:
            print "Case #%d: IMPOSSIBLE" % (caseNum + 1)
            continue
        i, swapCount = 0, 0
        blocked = False
        chicks.reverse()
        while i < len(chicks):
            
            fastEnough = wouldMakeIt(chicks[i], barnLocation, timeLimit)
            if fastEnough and not blocked:
                if i + 1 >= chickLimit:
                    break
                i += 1
            elif not fastEnough:
                blocked = True
                i += 1
            elif fastEnough and blocked:
                while i > 0 and not wouldMakeIt(chicks[i-1], barnLocation, timeLimit):
                    chicks[i], chicks[i-1] = chicks[i-1], chicks[i]
                    swapCount += 1
                    i -= 1
                blocked = False
        print "Case #%d: %d" % (caseNum + 1, swapCount)
    f.close()

def wouldMakeIt(chick, barnLocation, timeLimit):
    location, speed = chick
    distance = barnLocation - location
    if distance / speed < timeLimit:
        return True
    if distance / speed == timeLimit and distance % speed == 0:
        return True
    return False

main(sys.argv[1])

