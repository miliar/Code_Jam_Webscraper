import sys

def main():
    f = open(sys.argv[1], "r")
    cases = int(f.readline())
    for caseNum in xrange(cases):
        numberOfWires = int(f.readline())
        wires = []
        for i in xrange(numberOfWires):
            fromWindow, toWindow = map(int, f.readline().split())
            wires.append((fromWindow, toWindow))
        # sort if neccessary
        wires.sort(cmp=orderWires)
        intersectCount = 0
        for i in xrange(len(wires)):
            startPoint, endPoint = wires[i]
            j = i + 1
            while j < numberOfWires:
                bStartPoint, bEndPoint = wires[j]
                #if bStartPoint > endPoint:
                #    break
                if bEndPoint < endPoint:
                    intersectCount += 1
                j += 1
        print "Case #%d: %d" % (caseNum + 1, intersectCount)
    f.close()

def orderWires(a, b):
    if a[0] > b[0]:
        return 1
    if a[0] < b[0]:
        return -1
    return 0

main()
            