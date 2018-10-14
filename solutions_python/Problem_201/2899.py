from sortedcontainers import SortedList as SL

T = int(raw_input().strip())
for test in xrange(T):
    N,K = map(int,raw_input().strip().split())
    occupied = SL()
    occupied.update([0,N+1])
    for k in xrange(K):
        largestRange = 0
        bestStall = None
        for occLeft,occRight in zip(occupied[:-1],occupied[1:]):
            #print occupied,occLeft,occRight
            if occRight - occLeft > largestRange:
                largestRange = occRight-occLeft
                bestStall = (occRight-occLeft)/2+occLeft
        occupied.add(bestStall)

    idx = occupied.index(bestStall)
    LS = bestStall-occupied[idx-1]-1
    RS = occupied[idx+1]-bestStall-1
    print 'Case #%d: %d %d' % (test+1,max(LS,RS),min(LS,RS))


