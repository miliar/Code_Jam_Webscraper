t = int(raw_input())

def flip(p):
    if p == '+':
        return '-'
    else :
        return '+'

for i in xrange(1, t + 1):
    flipCount = 0
    ps, ks = raw_input().split(" ")
    k = int(ks)
    pancakes = list(ps)
    pstart = 0
    numPancakes = len(pancakes)
    while True:
        #print pancakes, k, flipCount, pstart, numPancakes
        while pancakes[pstart] == '+'  and pstart < numPancakes -1:
            pstart  = pstart + 1
        if (pstart == numPancakes -1 and pancakes[numPancakes-1] =='+'  ):
            print "Case #{}: {}".format(i, flipCount)
            break
        if (pstart > numPancakes -k ):
            print "Case #{}: {}".format(i, "IMPOSSIBLE")
            break
        # Now  pancakes[pstart] is ppoiting to blank side pancakes
        if (pstart + k < numPancakes+1):
            flipCount = flipCount +1
            for j in xrange(0, k):
                pancakes[pstart+j]  = flip (pancakes[pstart+j] )
